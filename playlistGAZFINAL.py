#!/usr/bin/env python

import os
import glob
import subprocess
from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)


GPIO.add_event_detect(23, GPIO.RISING, bouncetime=650)
GPIO.add_event_detect(24, GPIO.RISING, bouncetime=650)

os.chdir('/home/pi')
f = glob.glob('*.WAV')
h=len(f)
flag=1
pt=0
st=0

while True:
	if flag==1:
		player=subprocess.Popen(["omxplayer", '-o', 'local', f[pt]],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
		fi=player.poll()
		flag=0
		st=0
	
	if (GPIO.input(23)==True):
		sleep(0.5)
		fi=player.poll()
		if ((fi!=0) and (st!=1)):
			os.system('killall omxplayer.bin')
			st=1
		else:
			flag=1 # play
			
	if (GPIO.input(24)==True):
		fi=player.poll()
		if ((st==0) and (fi!=0)):
			os.system('killall omxplayer.bin')
		flag=1
		pt=pt+1
		if pt>h-1:
			pt=0
		sleep(0.5)
									

