#!/usr/bin/env python
import sys, rospy
from std_msgs.msg import UInt16

def leds(num=0):
	ledf0 = "/dev/rtled0"
	ledf1 = "/dev/rtled1"
	ledf2 = "/dev/rtled2"
	ledf3 = "/dev/rtled3"
	try:
		with open(ledf0,"w") as f:
			f.write(str(num) + "\n")
		with open(ledf1,"w") as f:
			f.write(str(num) + "\n")
		with open(ledf2,"w") as f:
			f.write(str(num) + "\n")
        	with open(ledf3,"w") as f:
                	f.write(str(num) + "\n") 
        except IOError:
                rospy.logerr("cannot write")

def recv_leds(data):
	leds(data)

if __name__  ==  '__main__':
	rospy.init_node('leds')
	rospy.Subscriber("leds", UInt16, recv_leds)
	rospy.spin()
