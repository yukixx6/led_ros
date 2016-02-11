#!/usr/bin/env python
import time
import sys
import rospy


ledf0 = [ "/dev/rtled0"]
ledf1 = [ "/dev/rtled1"]
ledf2 = [ "/dev/rtled2"]
ledf3 = [ "/dev/rtled3"]

a = raw_input()
x = int(a)

while x>0:
 for ledname0 in ledf0:
        with open(ledname0,'w') as f:
                f.write("1") 
 
 for ledname1 in ledf1:
        with open(ledname1,'w') as f:
                f.write("1")

 for ledname2 in ledf2:
        with open(ledname2,'w') as f:
                f.write("1")

 for ledname3 in ledf3:
        with open(ledname3,'w') as f:
                f.write("1")
 
	time.sleep(0.2)

 for ledname0 in ledf0:
        with open(ledname0,'w') as f:
                f.write("0")

 for ledname1 in ledf1:
        with open(ledname1,'w') as f:
                f.write("0")

 for ledname2 in ledf2:
        with open(ledname2,'w') as f:
                f.write("0")

 for ledname3 in ledf3:
        with open(ledname3,'w') as f:
                f.write("0")
		x -= 1
	time.sleep(0.2)
