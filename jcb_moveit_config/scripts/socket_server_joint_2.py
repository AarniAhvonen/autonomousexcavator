#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Vector3
import socket
import pickle
from datetime import datetime
from std_msgs.msg import Int32
import time




JOINT_VALUES = []

def callback(msg):
    print('Entered Callback')
    global serverSocket
    global clientConnection
    global datetime1
    global i
    #global JOINT_VALUES
    rospy.loginfo('Getting the joint values')
    joint_value = [msg.x, msg.y, msg.z]
    #JOINT_VALUES.append(joint_value)
    rospy.loginfo(f'Outputing the list of joint values {joint_value}')
    #datetime1 = datetime.now()

    rospy.loginfo(f'i value is  {i}')
    rospy.loginfo(f'count value is  {count}')

    try:
        data = pickle.dumps(joint_value)
        clientConnection.send(data)
        i = i + 1

        if i == count:
            print('abc')
            time.sleep(0.3)
            msg1 = "end"
            msg1bytes = str.encode(msg1)
            print('def')
            clientConnection.send(msg1bytes)
            print('ghi')
            #serverSocket.close()
            socket_re_init()



    except:
        print('exception')
        socket_re_init()




def callback_count(msg):
    print('got count')
    global count
    count = msg.data
    #return count


def listener():
    #while not rospy.is_shutdown():
    print('looping1')
    global count
    global count_c
    global clientConnection

    global i



    rospy.loginfo('Initing joint_values node')


    rospy.init_node('get_joint_values')
    sub_2 = rospy.Subscriber('/planned_joint_values_count', Int32, callback_count)
    sub = rospy.Subscriber('/planned_joint_positions', Vector3, callback)


    rospy.loginfo(f'i value is  {i}')
    rospy.loginfo(f'count value is  {count}')

    print('looping')

    rospy.spin()


    """
    datetime2 = datetime.now()
    if i == 0:
        datetime1=datetime2

    diff = datetime2 - datetime1
    # Get the interval in milliseconds
    diff_in_milli_secs = diff.total_seconds() * 1000
    print(diff_in_milli_secs)
    """




def socket_re_init():

    print('Re-initialising')
    """
    global serverSocket
    serverSocket = socket.socket()

    print("Server socket created")

    # Associate the server socket with the IP and Port

    ip = "192.168.0.51"

    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serverSocket.bind((ip, port))

    print("Server socket bound with with ip {} port {}".format(ip, port))
    """
    serverSocket.listen()

    msg1 = "end"
    msg1bytes = str.encode(msg1)
    clientConnection.send(msg1bytes)

    global count
    global count_c
    global i
    i = 0
    count_c = 0
    count = -1

    print('Looking for client connection')
    (clientConnection, clientAddress) = serverSocket.accept()

    count_c = count_c + 1

    print("Accepted {} connections so far".format(count_c))

    listener()


if __name__ == '__main__':

    print('In main')

    # Create a server socket
    serverSocket = socket.socket()

    print("Server socket created")

    # Associate the server socket with the IP and Port

    ip = "192.168.0.51"

    port = 35496
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serverSocket.bind((ip, port))

    print("Server socket bound with with ip {} port {}".format(ip, port))

    serverSocket.listen()


    # Server incoming connections "one by one"

    global count
    global i
    i = 0
    count_c=0
    count=-1

    print('Looking for client connection')
    (clientConnection, clientAddress) = serverSocket.accept()

    count_c = count_c + 1

    print("Accepted {} connections so far".format(count_c))

    listener()
