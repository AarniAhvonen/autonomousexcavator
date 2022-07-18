#! /usr/bin/env python
# joint_planning.py

#! /usr/bin/env python

import sys
import rospy
import socket
import pickle
import moveit_msgs.msg
import moveit_commander
from amps_to_angle import amps_to_angle
from geometry_msgs.msg import PoseStamped

def publish_scene(scene):
    print("Scene")
    print(scene.get_objects())
    if scene.get_objects():
        if "floor" in scene.get_objects():
            rospy.loginfo("The floor existed")
            return True
    else:
        rospy.loginfo("Building the object")
        # publish a scene
        pub_scene = PoseStamped()
        pub_scene.header.frame_id = robot.get_planning_frame()

        # add a table the block is at first
        pub_scene.pose.position.x = -0.5
        pub_scene.pose.position.y = 0
        pub_scene.pose.position.z = -0.1
        scene.add_box("floor", pub_scene, (4, 4, 0.2))
        rospy.sleep(1)
        rospy.loginfo("Added the floor")
        # rospy.loginfo(pub_scene)
        print("Scene")
        print(scene.get_objects())

        if scene.get_objects():
            if "floor" in scene.get_objects():
                rospy.loginfo("Add floor succeeded")
                return True
            else:
                return False
        else:
            rospy.loginfo("The scene is not pulished, start publishing again")
            publish_scene(scene)
            return False


if __name__ =='__main__':
    # data = [-1.5708, 0, 0]

    # angle_data = [-0.6526842563635249, -0.9481576253866109, -1]
    # print(angle_data)
    
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_test',
                    anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene12 = moveit_commander.PlanningSceneInterface()
    print("here is pub scene")
    publish_scene(scene12)
    print("here is the end of pub scene")
    arm = moveit_commander.MoveGroupCommander("arm")
    display_trajectory_publisher = rospy.Publisher(
        '/move_group/display_planned_path',
        moveit_msgs.msg.DisplayTrajectory, 
        queue_size=1)
    # group_variable_values_arm = arm.get_current_joint_values()
    # group_variable_values_arm[0] = angle_data[0]
    # group_variable_values_arm[1] = angle_data[1]
    # group_variable_values_arm[2] = angle_data[2]
    # arm.set_joint_value_target(group_variable_values_arm)
    # plan = arm.plan()
    # arm.go(wait=True)
    moveit_commander.roscpp_shutdown()



# import sys
# import rospy
# import moveit_commander
# import moveit_msgs.msg


# print("=================================================")
# print("================Start initializing===============")
# print("=================================================")
# joint_state_topic = ['joint_states:=/handy/joint_states']
# moveit_commander.roscpp_initialize(joint_state_topic)
# moveit_commander.roscpp_initialize(sys.argv)
# rospy.init_node('move_group_python_interface',
#                 anonymous=True)

# robot = moveit_commander.RobotCommander()
# scene = moveit_commander.PlanningSceneInterface()    
# arm = moveit_commander.MoveGroupCommander("handy_arm")
# hand = moveit_commander.MoveGroupCommander("handy_hand")
# display_trajectory_publisher = rospy.Publisher(
#     '/move_group/display_planned_path',
#     moveit_msgs.msg.DisplayTrajectory, queue_size=1)
# print("=================================================")
# print("============Initialization is done===============")
# print("=================================================")
# rospy.sleep(2)

# print("=================================================")
# print("=======Set arm joints values, start moving=======")
# print("=================================================")
# group_variable_values_arm = arm.get_current_joint_values()
# group_variable_values_arm[0] = 0.1
# group_variable_values_arm[1] = 0
# group_variable_values_arm[2] = 1.5708
# arm.set_joint_value_target(group_variable_values_arm)
# plan = arm.plan()
# arm.go(wait=True)
# print("=================================================")
# print("=======Set hand joints values, start moving======")
# print("=================================================")
# group_variable_values_hand = \
#     hand.get_current_joint_values()
# group_variable_values_hand[0] = -0.5
# group_variable_values_hand[1] = 0.5
# hand.set_joint_value_target(group_variable_values_hand)
# plan = hand.plan()
# hand.go(wait=True)
# rospy.sleep(1)
# print("=================================================")
# print("====Move robot by setting joints successfully====")
# print("=================================================")

# print("=================================================")
# print("=========Try to move the arm with set pose=======")
# print("=================================================")
# # replace the name "bow" to the name you set while
# # defining the poses
# arm.set_named_target("bow")
# arm.go(wait=True)
# rospy.sleep(1)
# moveit_commander.roscpp_shutdown()