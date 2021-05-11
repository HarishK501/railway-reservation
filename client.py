import socket

SERVER = "127.0.0.1"
PORT = 1247
client = socket.socket()
# client.bind(("localhost", 8080))

client.connect((SERVER, PORT))
# print(client.getsockname())
line = "---------------------------------------"
options = line + "\n1. Get train info\n2. Find trains\n3. Book Ticket\n4. Cancel Reservation\n" 
print("Hi user!\nWelcome to Railway Reservation Portal!\n")

while True:
    print(options)
    try:
        op = input("\n>>> ")
    except:
        print("Connection closed")
        break

    try:

        if op == '1':  # get train info
            num = input("➡  Enter train number: ")
            req = "getTrainInfo/" + num
            client.sendall(bytes(req, 'UTF-8'))
            in_data = client.recv(1024)
            res = in_data.decode()
            print(res)


        elif op == '2':  # find trains
            src = input("➡  Enter origin station: ")
            dest = input("➡  Enter destination: ")
            req = "findTrains/" + src + "&" + dest
            client.sendall(bytes(req, 'UTF-8'))
            in_data = client.recv(1024)
            res = in_data.decode()
            print(res)
            

    except:
        print("Connection closed")
        break

client.close()
