#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def subscriberCallBack(data):
    rospy.loginfo(rospy.get_caller_id() + " I recieved -- %s", data.data)

def listener():
    rospyinit_node('subscriberNode', anonymous=True)
    rospy.Subscriber("talker", String, subscriberCallBack)
    rospy.spin()

if __name__ == '__main__':
    listener()