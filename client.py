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
            if res == 'NULL':
                res = "<-- No train found with the given stations -->"
            print(res)

        elif op == '3':  # book ticket
            print("Enter login credentials:")
            username = input("➡  Username: ")
            password = input("➡  Password: ")
            req = "login/" + username + "&" + password
            client.sendall(bytes(req, 'UTF-8'))
            in_data = client.recv(1024)
            res = in_data.decode()
            if res == 'OK':
                print("Logged in successfully!\n")
                src = input("➡  Enter origin station: ")
                dest = input("➡  Enter destination: ")
                req = "findTrains/" + src + "&" + dest
                client.sendall(bytes(req, 'UTF-8'))
                in_data = client.recv(1024)
                res = in_data.decode()
                if res == 'NULL':
                    res = "<-- No train found with the given stations -->"
                    print(res)
                    continue
                print(res)
                train = input("➡  Choose a train (Enter train number): ")
                seats = input("➡  Enter number of seats: ")
                req = "checkTrain/" + train + "#" + seats
                client.sendall(bytes(req, 'UTF-8'))
                in_data = client.recv(1024)
                res = in_data.decode()
                if res == "OK":
                    print("Seats available!")
                    choice = input("➡  Book the tickets? (y/n): ")
                    if choice == 'y':
                        req = "bookTicket/" + train + "#" + seats
                        client.sendall(bytes(req, 'UTF-8'))
                        in_data = client.recv(1024)
                        res = in_data.decode()
            

    except:
        print("Connection closed")
        break

client.close()
