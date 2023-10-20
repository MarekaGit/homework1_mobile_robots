#!/usr/bin/env python2 
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

count = 0
N = 0
alpha = 0

def sumup_callback(threshold):
    global count
    global N
    global alpha
    count += 1
    if count == N:
        result = alpha * (N * int(threshold.data))
        rospy.loginfo("The result is " + str(result))

if __name__ == '__main__':
    rospy.init_node("sumup_node")
    rospy.loginfo("Sumup node has been started")

    param_alpha = rospy.get_param('/sumup_node/ros__parameters/alpha')
    alpha = int(param_alpha)
    print("Alpha: " + str(alpha))

    param_N = rospy.get_param('/counter_node/ros__parameters/N')
    N = int(param_N)
    print("N: " + str(N))

    sub = rospy.Subscriber("/ros_basics/value", Int32, callback=sumup_callback)

    rospy.spin()
