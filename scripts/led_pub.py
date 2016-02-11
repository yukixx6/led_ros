#!/usr/bin/env python 
import sys, rospy
from led_ros.msg import LedValues

rospy.init_node('led_pub')
pub = rospy.Publisher('leds_vel', LedValues, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	data = LedValues()
	
	direction0 = raw_input('LED0 >>> ')
	data.led0 = int(direction0)
	
	direction1 = raw_input('LED1 >>> ')
	data.led1 = int(direction1)

	direction2 = raw_input('LED2 >>> ')
	data.led2 = int(direction2)
	
	direction3 = raw_input('LED3 >>> ')
	data.led3 = int(direction3)
	
	print ('changed')
	print ('\n')
	pub.publish(data)

