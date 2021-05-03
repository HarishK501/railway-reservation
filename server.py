import socket
import threading


class MyServer:
    clients = []
    server = socket.socket()

    @staticmethod
    def startServer(port):
        MyServer.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        MyServer.server.bind(("127.0.0.1", port))
        print("Server started\nWaiting for client request..")
        MyServer.server.listen()
        while True:
            try:
                client, clientAddress = MyServer.server.accept()
                MyServer.clients.append(client)
                newthread = MyServer.ClientThread(client, clientAddress)
                newthread.start()
            except:
                print("Bye!")
                break

                

    class ClientThread(threading.Thread):
        def __init__(self, clientsocket, clientAddress):
            threading.Thread.__init__(self)
            self.csocket = clientsocket
            self.clientAddress = clientAddress
            print("New connection added: ", clientAddress)

        def run(self):
            # self.csocket.send(bytes("Hi, This is from Server..", 'utf-8'))
            msg = ''
            while True:
                try:

                    data = self.csocket.recv(2048)
                    msg = data.decode()
                    if msg == 'bye':
                        break
                    else:
                        self.csocket.send(bytes(msg[::-1], 'UTF-8'))
                        print("from client {}=>".format(self.clientAddress), msg)
                except:
                    break
                

            print("Client at ", self.clientAddress, " disconnected...")
            self.csocket.close()

if __name__ == "__main__":
    MyServer.startServer(1247)
