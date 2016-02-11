#!/usr/bin/env python
import sys, rospy
from led_ros.msg import LedValues

if __name__ == "__main__":
	devfile = "/dev/rtswitch0"
	rospy.init_node('switch')
	pub = rospy.Publisher('leds_vel', LedValues, queue_size=10)

	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		try:
			with open(devfile,'r') as f:
				f = [ int(e) for e in f ]
				d = LedValues()
				if f == [1]:
					d.led0 = 0
					d.led1 = 0
					d.led2 = 0
					d.led3 = 0
				if f == [0]:
					d.led0 = 1
					d.led1 = 1
					d.led2 = 1
					d.led3 = 1
			pub.publish(d)
		except IOError:
			rospy.logerr("cannot write to " + devfile)
		rate.sleep()
		
