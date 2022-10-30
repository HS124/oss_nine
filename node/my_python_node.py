#!/usr/bin/env python

import sys
import rospy

import actionlib

from geometry_msgs.msg import Twist

def update_timer(timer_event):
    print('update time')

rospy.init_node('my_python_node')

pub_cmd =rospy.Publisher('cmd_vel', Twist, queue_size=10)

twist = Twist()
txist = linear.x = 0.1
twist.angular.z = 0
pub_cmd.publish(twist)

rospy.spin()