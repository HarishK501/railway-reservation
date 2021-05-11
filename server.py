import socket
import threading
import pymongo

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
        loop = True
        while loop:
            try:
                client, clientAddress = MyServer.server.accept()
                MyServer.clients.append(client)
                newthread = MyServer.ClientThread(client, clientAddress)
                newthread.start()
            except:
                print("Bye!")
                break
            try:
                loop = int(input())
            except:
                break

    class ClientThread(threading.Thread):
        def __init__(self, clientsocket, clientAddress):
            threading.Thread.__init__(self)
            self.csocket = clientsocket
            self.clientAddress = clientAddress
            print("New connection added: ", clientAddress)

        def run(self):
            global trains
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
                            x = trains.find({'source': src, 'destination': dest})
                            if x == None:
                                self.csocket.send(bytes("<-- No train found with the given stations -->", 'utf-8'))
                            else:
                                x = list(x)
                                res = "\nNumber\tTrain name"
                                for t in x:
                                    res += '\n' + t['number'] + '\t' + t['name']
                                self.csocket.send(bytes(res, 'utf-8'))
                                
                except:
                    break

            print("Client at ", self.clientAddress, " disconnected...")
            self.csocket.close()


if __name__ == "__main__":
    myDB = connectDB("railDB")
    trains = myDB["trains"]
    MyServer.startServer(1247)
    
    # reservations = myDB["reservations"]
