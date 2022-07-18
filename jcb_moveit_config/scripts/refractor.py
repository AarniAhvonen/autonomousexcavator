#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Vector3
import socket
import pickle
from datetime import datetime
from std_msgs.msg import Int32
import time


def callback_count(msg):
    print('got count')
    global count
    count = msg.data

def callback(msg):
    print('Entered Callback')
    global serverSocket
    global clientConnection
    global i
    # global JOINT_VALUES
    rospy.loginfo('Getting the joint values')
    joint_value = [msg.x, msg.y, msg.z]
    # JOINT_VALUES.append(joint_value)
    rospy.loginfo(f'Outputing the list of joint values {joint_value}')
    # datetime1 = datetime.now()

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
            i=0
    except:
        print('exception')



if __name__ == "__main__":
    i=0
    rospy.init_node("test")
    serverSocket = socket.socket()
    print("Server socket created")
    serverSocket.settimeout(10000)
    # Associate the server socket with the IP and Port
    ip = "192.168.0.51"
    port = 35496
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((ip, port))
    print("Server socket bound with with ip {} port {}".format(ip, port))
    serverSocket.listen()

    sub_2 = rospy.Subscriber('/planned_joint_values_count', Int32, callback_count)
    sub = rospy.Subscriber('/planned_joint_positions', Vector3, callback)

    while not rospy.is_shutdown():
        while True:
            (clientConnection, clientAddress) = serverSocket.accept()
            print("Connected to cliennt")
