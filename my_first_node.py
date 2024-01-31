#!/usr/bin/env python
import rospy

if __name__ == '__main__':
    rospy.init_node('test_node')
    rospy.loginfo('Test Node has started')

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo('Hello ROS!')
        rate.sleep()