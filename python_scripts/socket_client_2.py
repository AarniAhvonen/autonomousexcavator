# import the socket module

import socket
import pickle

# Create a socket instance


socketObject = socket.socket()

# Using the socket connect to a server...in this case localhost

socketObject.connect(("192.168.0.51", 35496))

print("Connected to localhost")

# Send a message to the web server to supply a page as given by Host param of GET request

HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"

bytes = str.encode(HTTPMessage)

socketObject.sendall(bytes)

# Receive the data

while (True):

    recvd_data = socketObject.recv(1024)

    data = pickle.loads(recvd_data)

    print(data)

    if (data == b''):
        print("Connection closed")

        break

#socketObject.close()