#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('circle_node')
    rospy.loginfo('Node has started')

    rate = rospy.Rate(10)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        pub.publish(msg)
        rate.sleep()