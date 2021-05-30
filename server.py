import socket
import threading
import pymongo
from bson import ObjectId

def connectDB(db):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    myDB = myclient[db]
    return myDB


class MyServer:
    clients = []
    server = socket.socket()

    @staticmethod
    def startServer(port):
        MyServer.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        MyServer.server.bind(("127.0.0.1", port))
        print("Server started\nWaiting for client request..")
        MyServer.server.listen()
        # loop = 1
        while True:
            try:
                client, clientAddress = MyServer.server.accept()
                MyServer.clients.append(client)
                newthread = MyServer.ClientThread(client, clientAddress)
                newthread.start()
            except:
                print("Bye!")
                break
            # try:
            #     loop = int(input())
            # except:
            #     break

    class ClientThread(threading.Thread):
        def __init__(self, clientsocket, clientAddress):
            threading.Thread.__init__(self)
            self.csocket = clientsocket
            self.clientAddress = clientAddress
            print("New connection added: ", clientAddress)

        def run(self):
            global trains, users, reservations
            # welcomeMsg = "Hi user!\n1. Get train info\n"
            # self.csocket.send(bytes(welcomeMsg, 'utf-8'))
            msg = ''
            while True:
                try:
                    data = self.csocket.recv(2048)
                    msg = data.decode()
                    if msg == 'exit':
                        break
                    else:  
                        fn, val = msg.split("/")
                        if fn == "login":
                            usrname, passwd = val.split("&")
                            x = users.find_one({"username": usrname, "password": passwd})
                            if x == None:
                                self.csocket.send(bytes("NULL", 'utf-8'))
                            else:
                                x = dict(x)
                                self.csocket.send(bytes(str(x['_id']), 'utf-8'))

                        if fn == "getTrainInfo":
                            x = trains.find_one({'number': val})
                            if x == None:
                                self.csocket.send(bytes("<-- No train found with the given number -->", 'utf-8'))
                            else:
                                x = dict(x)
                                res = "\n"
                                for key in x.keys():
                                    if str(key) == "_id":
                                        continue
                                    res += str(key).capitalize() + "\t\t: " + str(x[key]) + "\n"
                                self.csocket.send(bytes(res, 'utf-8'))
                            
                        elif fn == "findTrains":
                            src, dest = val.split("&")
                            x = trains.find_one({'source': src, 'destination': dest})
                            if x == None:
                                self.csocket.send(bytes("NULL", 'utf-8'))
                            else:
                                x = trains.find({'source': src, 'destination': dest})
                                x = list(x)
                                res = "\narr\tdept\tNumber\tTrain name"
                                for t in x:
                                    res += '\n' + t['arrival_time'] + "\t" + t['departure_time'] + "\t" +t['number'] + '\t' + t['name']
                                self.csocket.send(bytes(res, 'utf-8'))

                        elif fn == "checkTrain":
                            train, seats = val.split("#")
                            seats = int(seats)
                            x = trains.find_one({'number': train})
                            if x == None:
                                self.csocket.send(bytes("404", 'utf-8'))
                            else:
                                x = dict(x)
                                if x["available_seats"] < seats:
                                    self.csocket.send(bytes("NULL", 'utf-8'))
                                else:
                                    self.csocket.send(bytes("OK", 'utf-8'))
                        
                        elif fn == "bookTicket":
                            train, seats, user = val.split("#")
                            seats = int(seats)
                            x = trains.find_one({'number': train})
                            if x == None:
                                self.csocket.send(bytes("404", 'utf-8'))
                            else:
                                x = dict(x)
                                if x["available_seats"] < seats:
                                    self.csocket.send(bytes("NULL", 'utf-8'))
                                else:
                                    # trains.find_one_and_update({'number': train}, {'available_seats': (x["available_seats"]-seats)})
                                    trains.update_one({'number': train}, {'$set': {"available_seats": (x["available_seats"]-seats)}})
                                    ticket = {
                                        "user": user,
                                        "train": train,
                                        "seats": seats
                                    }
                                    t = reservations.insert_one(ticket)
                                    self.csocket.send(bytes("Seats booked!\nTicket id: {}".format(str(t.inserted_id)), 'utf-8'))

                        elif fn == "checkTicket":
                            x = reservations.find_one({"_id": ObjectId(val)})
                            if x == None:
                                self.csocket.send(bytes("404", 'utf-8'))
                            else:
                                self.csocket.send(bytes("OK", 'utf-8'))

                        elif fn == "cancelTicket":
                            x = reservations.find_one({"_id": ObjectId(val)})
                            if x == None:
                                self.csocket.send(bytes("404", 'utf-8'))
                            else:
                                tr = trains.find_one({"number": x["train"]})
                                x = dict(x)
                                tr = dict(tr)
                                trains.update_one({"number": x["train"]}, {'$set': {"available_seats": (tr["available_seats"]+x["seats"])}})
                                reservations.delete_one({"_id": ObjectId(val)})
                                self.csocket.send(bytes("OK", 'utf-8'))

                except:
                    break

            print("Client at ", self.clientAddress, " disconnected...")
            self.csocket.close()


if __name__ == "__main__":
    myDB = connectDB("railDB")
    trains = myDB["trains"]
    users = myDB["login"]
    reservations = myDB["reservations"]
    MyServer.startServer(1247)
    
    # reservations = myDB["reservations"]
