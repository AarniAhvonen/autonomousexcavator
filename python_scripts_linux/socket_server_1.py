import socket
import pickle

# Create a server socket

serverSocket = socket.socket()

print("Server socket created")

# Associate the server socket with the IP and Port

ip = "192.168.0.51"

port = 35491

serverSocket.bind((ip, port))

print("Server socket bound with with ip {} port {}".format(ip, port))

# Make the server listen for incoming connections

serverSocket.listen()

# Server incoming connections "one by one"

count = 0

while (True):

    (clientConnection, clientAddress) = serverSocket.accept()

    count = count + 1

    print("Accepted {} connections so far".format(count))

    # read from client connection

    while (True):

        data = clientConnection.recv(1024)

        print(data)

        if (data != b''):
            msg1 = "Excavator Digitally"

            msg1Bytes = str.encode(msg1)

            msg2 = "Connection Successful"

            msg2Bytes = str.encode(msg2)

            #clientConnection.send(msg1Bytes)

            #clientConnection.send(msg2Bytes)

            for var in range(3):
                y = [var, var+1, var+2]
                print(y)

                
            #y = [0, 12, 6, 8, 3, 2, 10]
            data = pickle.dumps(y)
            clientConnection.send(data)

            print("Connection closed")

            break