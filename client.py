import socket

SERVER = "127.0.0.1"
PORT = 1247
client = socket.socket()
# client.bind(("localhost", 8080))

client.connect((SERVER, PORT))
# print(client.getsockname())
options = "1. Get train info"
print("Hi user!\n"+options)

while True:
    try:
        op = input("\n>>> ")
        if op == "options":
            print(options)
        elif (op == "1"):
            num = input("- Enter train number: ")
            req = "getTrainInfo/"+num
            client.sendall(bytes(req, 'UTF-8'))
            try:
                in_data = client.recv(1024)
                res = in_data.decode()
                print(res)
            except:
                print("Connection closed")
                break
    except:
        print("Connection closed")
        break



client.close()
