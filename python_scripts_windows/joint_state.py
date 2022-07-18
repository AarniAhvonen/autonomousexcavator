#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

def callback(msg):
    print(msg.position)
        #print("success")

def listener():
    rospy.init_node('join_states')
    print('a')
    sub = rospy.Subscriber('/joint_states', JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()





