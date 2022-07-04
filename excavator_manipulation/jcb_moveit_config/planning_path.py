import sys
import rospy
import argparse
import moveit_msgs.msg
import geometry_msgs.msg
from moveit_commander import RobotCommander, MoveGroupCommander, \
    PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from tf.transformations import quaternion_from_euler


class ControlRobot():
    def __init__(self):
        roscpp_initialize(sys.argv)
        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        self.group = MoveGroupCommander("arm")
        self.display_trajectory_publisher = rospy.Publisher(
            '/move_group/display_planned_path',
            moveit_msgs.msg.DisplayTrajectory, 
            queue_size=1)

    def set_target(self, x, y, z, roll, pitch, yaw):
        pose_target = geometry_msgs.msg.Pose()
        pose_target.position.x = x
        pose_target.position.y = y
        pose_target.position.z = z
        q = quaternion_from_euler(roll, pitch, yaw)
        pose_target.orientation.x = q[0]
        pose_target.orientation.y = q[1]
        pose_target.orientation.z = q[2]
        pose_target.orientation.w = q[3]
        return pose_target

    def plan_and_go(self, x, y, z, roll, pitch, yaw):
        pose_target = self.set_target(x, y, z, roll, pitch, yaw)
        self.group.set_pose_target(pose_target)
        self.group.allow_replanning(True)
        self.group.allow_looking(True)
        self.group.plan()
        rospy.sleep(3)
        self.group.go(wait=True)


if __name__=='__main__':
    # Get the position and the value of roll, pitch, and yaw.
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--position_x", type=float, required=True, 
                        help="an float for the position of x")
    parser.add_argument("-y", "--position_y", type=float, required=True,
                        help="an float for the position of y")
    parser.add_argument("-z", "--position_z", type=float, required=True,
                        help="an float for the position of z")
    parser.add_argument("-r", "--roll", type=float, required=True,
                        help="an float for the value of roll")
    parser.add_argument("-p", "--pitch", type=float, required=True,
                        help="aan float for the value of pitch")
    parser.add_argument("-ya", "--yaw", type=float, required=True,
                        help="an float for the value of yaw")
    args = parser.parse_args()
    print(type(args.position_x))
    control_robot = ControlRobot()
    # Assign the position and the value of roll, pitch, and yaw.
    control_robot.plan_and_go(float(args.position_x), args.position_y,
        args.position_z, args.roll, args.pitch, args.yaw)
    roscpp_shutdown()
