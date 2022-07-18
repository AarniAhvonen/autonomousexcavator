import socket
import pickle
import time

# Create a server socket

serverSocket = socket.socket()

print("Server socket created")

# Associate the server socket with the IP and Port

ip = "192.168.0.51"

port = 35496
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
            """msg1 = "Excavator Digitally"

            msg1Bytes = str.encode(msg1)

            msg2 = "Connection Successful"

            msg2Bytes = str.encode(msg2)

            clientConnection.send(msg1Bytes)

            clientConnection.send(msg2Bytes)
            """
            print('a')
            for var in range(5):
                y = [var, var + 1, var + 2]
                print(y)
                data = pickle.dumps(y)
                clientConnection.send(data)
                if var==4:
                    msg1 = "end"
                    msg1Bytes = str.encode(msg1)
                    clientConnection.send(msg1Bytes)

                time.sleep(0.1)




            # y = [0, 12, 6, 8, 3, 2, 10]
            #data = pickle.dumps(y)
            #clientConnection.send(data)

            print("Connection closed")

            break