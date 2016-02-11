#!/usr/bin/env python
import sys, rospy
from led_ros.msg import LedValues


def write_led0(a=0):
	ledf0 = "/dev/rtled0"
	try:
		with open(ledf0,"w") as f:
			f.write(str(a) + "\n")
        except IOError:
                rospy.logerr("cannot write" + ledf0)

def write_led1(b=0):
	ledf1 = "/dev/rtled1"
        try: 
	        with open(ledf1,"w") as f:
                	f.write(str(b) + "\n")
        except IOError:
                rospy.logerr("cannot write" + ledf1)

def write_led2(c=0):
        ledf2 = "/dev/rtled2"
        try:
                with open(ledf2,"w") as f:
                        f.write(str(c) + "\n")
        except IOError:
                rospy.logerr("cannot write" + ledf2)

def write_led3(d=0):
        ledf3 = "/dev/rtled3"
        try:
                with open(ledf3,"w") as f:
                        f.write(str(d) + "\n")
        except IOError:
                rospy.logerr("cannot write" + ledf3)

data = LedValues()

def recv_led0(data):
	write_led0(data.led0)
def recv_led1(data):
	write_led1(data.led1)
def recv_led2(data):
	write_led2(data.led2)
def recv_led3(data):
	write_led3(data.led3)

if __name__  ==  '__main__':
	rospy.init_node('leds')
	rospy.Subscriber("leds_vel", LedValues, recv_led0)
        rospy.Subscriber("leds_vel", LedValues, recv_led1)
        rospy.Subscriber("leds_vel", LedValues, recv_led2)
        rospy.Subscriber("leds_vel", LedValues, recv_led3)
	rospy.spin()
