import socket

SERVER = "127.0.0.1"
PORT = 1247
client = socket.socket()
# client.bind(("localhost", 8080))

client.connect((SERVER, PORT))
# print(client.getsockname())

while True:
    out_data = input("\n>>> ")
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        print("Closing connection...")
        break

    try:
        in_data = client.recv(1024)
        res = in_data.decode()
        print("Other client :", res)
    except:
        print("Connection closed")
        break


client.close()
