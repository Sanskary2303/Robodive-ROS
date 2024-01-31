#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def webcam_publisher():
    rospy.init_node('webcam_publisher', anonymous=True)

    image_pub = rospy.Publisher('webcam/image', Image, queue_size=10)

    cap = cv2.VideoCapture(0)

    bridge = CvBridge()

    rate = rospy.Rate(30)  

    while not rospy.is_shutdown():
        ret, frame = cap.read()

        if ret:
            ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")

            image_pub.publish(ros_image)

            rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        webcam_publisher()
    except rospy.ROSInterruptException:
        pass
