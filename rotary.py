#!/usr/bin/python3
import RPi.GPIO as GPIO  
import math, sys, os
import subprocess
import socket
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

st = 0
pt = 0 
c=0
last = 1
number = ""
x = len(number)
flag = 0

def count(pin):
    global c
    c = c + 1

GPIO.add_event_detect(18, GPIO.BOTH)

while True:
    try:
        if ((GPIO.input(5)==True)):
            #print("trubka NE cnata")
            if (pt == 0):
                start = subprocess.Popen(['omxplayer','-o','alsa', '/home/pi/tone.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                start.poll()
                sleep(5)
                pt = 1
            os.system('killall omxplayer.bin')
            c = 0
            number = ""
            flag = 1
            st = 0
            sleep(0.5)
        if ((GPIO.input(5)==False)):
            #print("trubka cnata")
            if (flag == 1 and st == 0):
                os.system('killall omxplayer.bin')
                voice = subprocess.Popen(['omxplayer','-o','alsa', '/home/pi/nabor.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                voice.poll()
                flag = 0
            if GPIO.event_detected(18):
                current = GPIO.input(18)
                flag = 0
                os.system('killall omxplayer.bin')
                print("18detected")
                if(last != current):
                    if(current == 0):
                        GPIO.add_event_detect(23, GPIO.BOTH, callback=count, bouncetime=20)
                        print("23detected")
                    else:
                        GPIO.remove_event_detect(23)
                        print("3")
                        if math.floor(c / 2) == 10:
                            number += "0"
                            x = len(number)
                            if x >= 5:
                                number = ""
                                number += "0"
                        else:
                            number += str(math.floor(c / 2))
                            x = len(number)
                            if x >= 5:
                                number = ""
                                number += str(math.floor(c / 2))
                                       
                        print (number)
                        if ((number == "1941") and flag == 0 and st == 0):
                            print('YES')
                            os.system('killall omxplayer.bin')
                            voice = subprocess.Popen(['omxplayer','-o','alsa','/home/pi/1.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                            st = 1
                        
                        if ((number == "1942") and flag == 0 and st == 0):
                            print('YES2')
                            os.system('killall omxplayer.bin')
                            voice = subprocess.Popen(['omxplayer','-o','alsa','/home/pi/2.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                            st = 1
                            
                            
                        if ((number == "1943") and flag == 0 and st == 0):
                            print('YES3')
                            os.system('killall omxplayer.bin')
                            voice = subprocess.Popen(['omxplayer','-o','alsa','/home/pi/3.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                            st = 1
                            
                        if ((number == "1945") and flag == 0 and st == 0):
                            print('YES3')
                            os.system('killall omxplayer.bin')
                            voice = subprocess.Popen(['omxplayer','-o','alsa','/home/pi/4.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                            st = 1
                            
                        if ((number == "1976") and flag == 0 and st == 0):
                            print('YES3')
                            os.system('killall omxplayer.bin')
                            voice = subprocess.Popen(['omxplayer','-o','alsa','/home/pi/5.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                            st = 1
                            
                        if ((number == "1948") and flag == 0 and st == 0):
                            print('YES3')
                            os.system('killall omxplayer.bin')
                            voice = subprocess.Popen(['omxplayer','-o','alsa','/home/pi/6.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                            st = 1    
                            
                            
                        
                        if ((x >= 4) and number != "1941" and number != "1942" and number != "1943" and number != "1945" and number != "1976" and number != "1948" and flag == 0 and st == 0 ):
                            print("NEVERNY NOMER")
                            os.system('killall omxplayer.bin')
                            number = ""
                            number += str(math.floor(c / 2))
                            voice = subprocess.Popen(['omxplayer','-o','alsa','/home/pi/neverno.mp3'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                            voice.poll()
                            flag = 1
                            st = 1
                            
                            
                        
                        c = 0
                    
                    
                    last = GPIO.input(18)
            #else:
                #print('else')
                #if flag == 1:
        #sleep(1)
    except KeyboardInterrupt:
        break