#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Load all the GPIO inputs you want to test

GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

# debounce buttons and trigger the rising event,  since they can be noisy
GPIO.add_event_detect(4, GPIO.RISING, bouncetime=450)
GPIO.add_event_detect(17, GPIO.RISING, bouncetime=450)
GPIO.add_event_detect(27, GPIO.RISING, bouncetime=450)



print 'GPIO Tester - Press a button'

while True:
    if ( GPIO.input(04) == False ):
        print 'GPIO 04 Pressed'
    if ( GPIO.input(17) == False ):
        print 'GPIO 17 Pressed'
    if ( GPIO.input(27) == False):
        print 'GPIO 27 Pressed'
        
        
    sleep(0.5);