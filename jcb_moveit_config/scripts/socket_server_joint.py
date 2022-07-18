#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Vector3
import socket
import pickle
import time






JOINT_VALUES = []

def callback(msg):

    global clientConnection
    #global JOINT_VALUES
    rospy.loginfo('Getting the joint values')
    joint_value = [msg.x, msg.y, msg.z]
    #JOINT_VALUES.append(joint_value)
    rospy.loginfo(f'Outputing the list of joint values {joint_value}')

    data = pickle.dumps(joint_value)
    clientConnection.send(data)


def listener():
    global count
    global clientConnection
    (clientConnection, clientAddress) = serverSocket.accept()

    count = count + 1

    print("Accepted {} connections so far".format(count))

    rospy.loginfo('Initing joint_values node')
    rospy.init_node('get_joint_values')
    sub = rospy.Subscriber('/planned_joint_positions', Vector3, callback)
    rospy.spin()


if __name__ == '__main__':
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
    count = 0
    listener()