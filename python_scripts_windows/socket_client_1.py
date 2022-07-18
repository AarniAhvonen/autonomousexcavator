# import the socket module

import socket
import pickle

DATAS = list()
I = 0
# Create a socket instance
def client():

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
        print(f'This is the {recvd_data}')
        if recvd_data==b"end":
            break
        data = pickle.loads(recvd_data)
        DATAS.append(data)




    if (data == b''):
        print("Connection closed")

        #break

    #socketObject.close()

def recvd_data():
    global I
    #client()
    #for data in DATAS:
    print(I)
    print(DATAS[I])
    return DATAS[I]

def loop_return():
    global I
    #client()
    for i_num in range(len(DATAS)):
        recvd_data()
        I = I + 1


if __name__ == '__main__':
    client()
    loop_return()