#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

print "start"
GPIO.output(17, 0)
GPIO.output(27, 0)
 
UDP_PORT = 5003
UDP_IP = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
 
while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode('utf-8')
    if not data:
        break
    print("" + data)
    if data == 'POWERON':
        GPIO.output(27, 1)
        sleep(0.3)
        GPIO.output(27, 0)
        print "yes"
	 
sock.close()	 
