#!/usr/bin/python

from mpu6050 import *
import time
import subprocess
import os

mpu = MPU6050()
mpu.initialize()

# Set calibration data
mpu.gyro_offs = {'x': -178, 'y': 259, 'z': -104}
mpu.accel_offs =  {'y': -354, 'x': 389, 'z': -1482}

accel_data = mpu.get_accel()
x_rotation = mpu.get_x_rotation(accel_data)
y_rotation = mpu.get_y_rotation(accel_data)

last_time = time.time()
alpha = 0.95;

flag=1
pt=0
st=0

while True:
    global player1
    global player2
    global player3
	new_time = time.time()
	gyro_data = mpu.get_gyro()
	accel_data = mpu.get_accel()

	dt = new_time - last_time
	last_time = new_time
	gyro_angle_x = gyro_data['x']*dt + x_rotation
	gyro_angle_y = gyro_data['y']*dt + y_rotation

	x_rotation = alpha*gyro_angle_x + (1.0 - alpha)*mpu.get_x_rotation(accel_data)
	y_rotation = alpha*gyro_angle_y + (1.0 - alpha)*mpu.get_y_rotation(accel_data)

	print "x:", x_rotation
	print "y:", y_rotation
	
	time.sleep(0.05)
	
	if flag==1:
		player1=subprocess.Popen(['omxplayer','-b','--no-osd','/home/pi/videos/loop.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
		fi=player.poll()
		flag=0
	
	if (x_rotation >= 250 && y_rotation <= 150):
		if st==0:
			os.system('killall omxplayer.bin')   
		sleep(0.1)
		player2=subprocess.Popen(['omxplayer','-b','--no-osd','/home/pi/videos/loop.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
	
	elif (x_rotation <= -150 && y_rotation >= 250):
		if pt==0:
			os.system('killall omxplayer.bin')
		sleep(0.1)
		player3=subprocess.Popen(['omxplayer','-b','--no-osd','/home/pi/videos/video1.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
	
	else:
		fi=player.poll()
		if(st==0 and fi==0):
			flag=1
	sleep(0.1)	
			
