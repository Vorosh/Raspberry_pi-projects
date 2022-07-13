#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
import os
from threading import Thread
from omxplayer.player import OMXPlayer
from pathlib import Path
import time
import logging
logging.basicConfig(level=logging.INFO)

VIDEO_1_PATH = Path('/home/pi/2.mp4')
player_log = logging.getLogger('Player 1')
player = OMXPlayer(VIDEO_1_PATH, args=['--loop', '-b'], dbus_name='org.mpris.MediaPlayer2.omxplayer1')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig1 = 23
echo1 = 24

GPIO.setup(trig1, GPIO.OUT)
GPIO.setup(echo1, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(25, GPIO.IN)

def measure_distance1():
	global distance1
	GPIO.output(trig1, True)
	time.sleep(0.00001)
	GPIO.output(trig1, False)
	
	
	while (GPIO.input(echo1) == 0): pass
	
	start1 = time.time()
	
	while (GPIO.input(echo1) == 1): pass
	
	end1 = time.time()
	
	distance1 = ((end1 - start1)*34300)/2
	
	return distance1    


def loop():
	flag=1
	st=1
	pt=1
	while True:
		measure_distance1()
		print 'distance1 = %.1f cm' % distance1
		time.sleep(1.5)
		if (GPIO.input(14)==True):
                    if (distance1 >=0 and distance1 <10):
			if flag==1:
				time.sleep(1.0001)
				print 'play GPIO TRUE'
				player.set_position(25)
				flag=0
				st=1
				time.sleep(0.0001)
			elif flag==0:
				print 'communicate play GPIO TRUE'
				if player.is_playing:
                                    player.playEvent()
                                    if player.position()>45:
                                        print '>45 end GPIO TRUE'
                                        player.set_position(25)
				st=1
				pt=1
				
                    elif (distance1 >=10 and distance1 <20):
			if pt==1:
				time.sleep(1.0001)
				print 'play GPIO TRUE'
				player.set_position(50)
				pt=0
				st=1
				flag=1
				time.sleep(0.0001)
			elif pt==0:
				print 'communicate play GPIO TRUE'
				if player.is_playing:
                                    player.playEvent()
                                    if player.position()>70:
                                        print '> 70 end GPIO TRUE'
                                        player.set_position(50)
				st=1
				flag=1
				
                    else:
			if st==1:
				time.sleep(1.0001)
				print 'stop GPIO TRUE'
				player.set_position(100)
				st=0
				flag=1
				pt=1
				time.sleep(0.0001)
			elif st==0:
				print 'communicate stop GPIO TRUE'
				if player.is_playing:
                                    player.playEvent()
                                    if player.position()>120:
                                        print '> 120 end GPIO TRUE'
                                        player.set_position(100)
				flag=1
				pt=1
                    time.sleep(0.5)
                
                if (GPIO.input(25)==True):
                    if (distance1 >=0 and distance1 <10):
			if flag==1:
				time.sleep(1.0001)
				print 'play GPIO FALSE'
				player.set_position(145)
				flag=0
				st=1
				time.sleep(0.0001)
			elif flag==0:
				print 'communicate play GPIO FALSE'
				if player.is_playing:
                                    player.playEvent()
                                    if player.position()>165:
                                        print '>165 end GPIO FALSE'
                                        player.set_position(145)
				st=1
				pt=1
				
                    elif (distance1 >=10 and distance1 <20):
			if pt==1:
				time.sleep(1.0001)
				print 'play GPIO FALSE'
				player.set_position(195)
				pt=0
				st=1
				flag=1
				time.sleep(0.0001)
			elif pt==0:
				print 'communicate play GPIO FALSE'
				if player.is_playing:
                                    player.playEvent()
                                    if player.position()>215:
                                        print '> 215 end GPIO FALSE'
                                        player.set_position(195)
				st=1
				flag=1
				
                    else:
			if st==1:
				time.sleep(1.0001)
				print 'stop GPIO FALSE'
				player.set_position(360)
				st=0
				flag=1
				pt=1
				time.sleep(0.0001)
			elif st==0:
				print 'communicate stop GPIO FALSE'
				if player.is_playing:
                                    player.playEvent()
                                    if player.position()>380:
                                        print '> 385 end GPIO FALSE'
                                        player.set_position(360)
				flag=1
				pt=1
                time.sleep(0.5)
                    
	    

def destroy():
	GPIO.cleanup()


if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup()			