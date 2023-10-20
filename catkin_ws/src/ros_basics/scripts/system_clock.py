#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node("system_clock_node")
    rospy.loginfo("System clock node has been started")

    param_rate = rospy.get_param('/system_clock_node/ros__parameters/rate')
    rate = rospy.Rate(param_rate)
    print("Rate parameter: " + str(param_rate))
    
    pub = rospy.Publisher("/ros_basics/clock", Int32, queue_size=10)

    clock_value = -1
    
    while not rospy.is_shutdown():
        clock_value += 1
        rospy.loginfo("Clock: " + str(clock_value))
        pub.publish(clock_value)
        rate.sleep()
    
