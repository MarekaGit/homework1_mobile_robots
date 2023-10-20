#!/usr/bin/env python2 
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

value = 0
threshold = 0

def clock_callback(clock):
    global value
    global threshold

    value += 1
    if value == threshold:
        rospy.loginfo("Clock: " + str(clock) + ", Threshold: " + str(value))
        value_pub.publish(value)
    else:  
        rospy.loginfo("Clock: " + str(clock) + ", Value: " + str(value))

if __name__ == '__main__':
    rospy.init_node("counter_node")
    rospy.loginfo("Counter node has been started")

    param_init = rospy.get_param('/counter_node/ros__parameters/init_value')
    value = param_init
    print("Initial Value: " + str(value))

    param_threshold = rospy.get_param('/counter_node/ros__parameters/threshold')
    threshold = param_threshold
    print("Threshold: " + str(threshold))

    sub = rospy.Subscriber("/ros_basics/clock", Int32, callback=clock_callback)

    value_pub = rospy.Publisher("/ros_basics/value", Int32, queue_size=10)

    rospy.spin()
