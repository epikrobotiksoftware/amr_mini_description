#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan


def callback(msg):
    print(msg.ranges)


rospy.init_node('scan_values')
sub = rospy.Subscriber(
    '/amr_mini_description/front_lidar_amr_mini_laser', LaserScan, callback)
rospy.spin()
