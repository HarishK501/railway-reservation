import socket

SERVER = "127.0.0.1"
PORT = 1247
client = socket.socket()
# client.bind(("localhost", 8080))

client.connect((SERVER, PORT))
# print(client.getsockname())
line = "\n---------------------------------------"
options = line + "\n1. Get train info\n2. Find trains\n3. Book Ticket\n4. Cancel Reservation\n5. Exit portal" 
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
                res = "\n<-- No train found with the given stations -->"
            print(res)

        elif op == '3':  # book ticket
            print("Enter login credentials:")
            username = input("➡  Username: ")
            password = input("➡  Password: ")
            req = "login/" + username + "&" + password
            client.sendall(bytes(req, 'UTF-8'))
            in_data = client.recv(1024)
            res = u_id = in_data.decode()
            if not res == 'NULL':
                print("Logged in successfully!\n")
                src = input("➡  Enter origin station: ")
                dest = input("➡  Enter destination: ")
                req = "findTrains/" + src + "&" + dest
                client.sendall(bytes(req, 'UTF-8'))
                in_data = client.recv(1024)
                res = in_data.decode()
                if res == 'NULL':
                    res = "\n<-- No train found with the given stations -->"
                    print(res)
                    continue
                print(res + "\n")
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
                        req = "bookTicket/" + train + "#" + seats + "#" + u_id
                        client.sendall(bytes(req, 'UTF-8'))
                        in_data = client.recv(1024)
                        res = in_data.decode()
                        if res == "NULL":
                            print("Oops! {} seats are not available in the train".format(seats))
                        else:
                            print(res + "\nThe tickets will be sent to your mobile.")
                    elif choice == 'n':
                        print("Cancelling ticket reservation...")
                elif res == "NULL":
                    print("Oops! {} seats are not available in the train".format(seats))
                else:
                    print("Invalid train number!")
            else:
                print("Invalid credentials!!")

        elif op == '4': # cancel ticket
            print("Enter login credentials:")
            username = input("➡  Username: ")
            password = input("➡  Password: ")
            req = "login/" + username + "&" + password
            client.sendall(bytes(req, 'UTF-8'))
            in_data = client.recv(1024)
            res = in_data.decode()
            if not res == 'NULL':
                print("Logged in successfully!\n")
                ticket = input("➡  Enter ticket id: ")
                req = "checkTicket/" + ticket
                client.sendall(bytes(req, 'UTF-8'))
                in_data = client.recv(1024)
                res = in_data.decode()
                print()
                if res == "OK":
                    choice = input("Cancel ticket<{}> for {}? (y/n): ".format(ticket, username))
                    if choice == 'y':
                        req = "cancelTicket/" + ticket
                        client.sendall(bytes(req, 'UTF-8'))
                        in_data = client.recv(1024)
                        res = in_data.decode()
                        if res == "OK": 
                            print("Ticket cancelled successfully!")
                        else:
                            print("Oops! Some error occured. Try again!")
                    else:
                        print("Cancellation not done!")
                else:
                    print("Invalid ticket id!")

            else:
                print("Invalid credentials!!")

        elif op == '5': #exit
            print("Thank you!")
            break

    except:
        print("Connection closed")
        break

client.close()
