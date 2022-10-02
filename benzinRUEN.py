#!/usr/bin/python3

from time import sleep
import os
import glob
from threading import Lock, Thread
import threading
import subprocess
import RPi.GPIO as GPIO
import tkinter
from tkinter import *
import sys

root = Tk()
root["bg"] = "black"
root.geometry("1920x1080")
root.attributes('-fullscreen', True)
root.config(cursor="none")
root.bind('<Escape>',lambda e: root.destroy())

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(16, GPIO.IN) # switch button RU/EN

currentstate = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
flag6 = 0
flag7 = 0
flag8 = 0
komanda=0
languageState = 0
currentstate2 = 0

# debounce buttons and trigger the rising event,  since they can be noisy
GPIO.add_event_detect(23, GPIO.FALLING, bouncetime=1400)
GPIO.add_event_detect(24, GPIO.FALLING, bouncetime=1400)
GPIO.add_event_detect(22, GPIO.FALLING, bouncetime=1400)
GPIO.add_event_detect(27, GPIO.FALLING, bouncetime=1400)

GPIO.add_event_detect(16, GPIO.FALLING, bouncetime=1400) # switch button RU/EN

def ButtonPressed():
    global komanda
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    flag6 = 0
    flag7 = 0
    flag8 = 0
    while True:
        if ((GPIO.input(23) == False) and (GPIO.input(24) == False) and (GPIO.input(27) == False) and (GPIO.input(22) == True)) :
            if flag1 == 0:
                sleep(1)
                komanda = 1
                flag1 = 1
                flag2 = 0
                flag3 = 0
                flag4 = 0
                flag5 = 0
                flag6 = 0
                flag7 = 0
                flag8 = 0


        elif ((GPIO.input(23) == False) and (GPIO.input(24) == False) and (GPIO.input(27) == True) and (GPIO.input(22) == True)) :
            if flag2 == 0:
                sleep(1)
                komanda = 2
                flag1 = 0
                flag2 = 1
                flag3 = 0
                flag4 = 0
                flag5 = 0
                flag6 = 0
                flag7 = 0
                flag8 = 0

        elif ((GPIO.input(23) == False) and (GPIO.input(24) == True) and (GPIO.input(27) == False) and (GPIO.input(22) == True)) :
            if flag3 == 0:
                sleep(1)
                komanda = 7
                flag1 = 0
                flag2 = 0
                flag3 = 1
                flag4 = 0
                flag5 = 0
                flag6 = 0
                flag7 = 0
                flag8 = 0

        elif ((GPIO.input(23) == True) and (GPIO.input(24) == False) and (GPIO.input(27) == False) and (GPIO.input(22) == True)) :
            if flag4 == 0:
                sleep(1)
                komanda = 8
                flag1 = 0
                flag2 = 0
                flag3 = 0
                flag4 = 1
                flag5 = 0
                flag6 = 0
                flag7 = 0
                flag8 = 0

        elif ((GPIO.input(23) == False) and (GPIO.input(24) == False) and (GPIO.input(27) == True) and (GPIO.input(22) == False)) :
            if flag5 == 0:
                sleep(1)
                komanda = 3
                flag1 = 0
                flag2 = 0
                flag3 = 0
                flag4 = 0
                flag5 = 1
                flag6 = 0
                flag7 = 0
                flag8 = 0

        elif ((GPIO.input(23) == False) and (GPIO.input(24) == True) and (GPIO.input(27) == False) and (GPIO.input(22) == False)) :
            if flag6 == 0:
                sleep(1)
                komanda = 4
                flag1 = 0
                flag2 = 0
                flag3 = 0
                flag4 = 0
                flag5 = 0
                flag6 = 1
                flag7 = 0
                flag8 = 0

        elif ((GPIO.input(23) == True) and (GPIO.input(24) == False) and (GPIO.input(27) == False) and (GPIO.input(22) == False)) :
            if flag7 == 0:
                sleep(1)
                komanda = 5
                flag1 = 0
                flag2 = 0
                flag3 = 0
                flag4 = 0
                flag5 = 0
                flag6 = 0
                flag7 = 1
                flag8 = 0

        else:
            if flag8 == 0:
                sleep(1)
                komanda = 6
                flag1 = 0
                flag2 = 0
                flag3 = 0
                flag4 = 0
                flag5 = 0
                flag6 = 0
                flag7 = 0
                flag8 = 1

def PlayerStart():
    global komanda
    global currentstate
    global currentstate2
    global languageState
    currentstate = 0
    while True:
        if GPIO.input(16) == False and currentstate2 == 1:
            languageState = not languageState
            sleep(1)
            print(languageState)
            currentstate2 = 0
            currentstate = 0

        if GPIO.input(16) == True and currentstate2 == 0:
            currentstate2 = 1
            print('currentstate2 = 1')

        if (komanda == 1 and currentstate != 1):
            print('play loop')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/loop.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU loop")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/loop.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN loop")
            currentstate = 1

        elif (komanda == 2 and currentstate != 2):
            print('play vstavte')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/zastavka1.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU zastavka")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/zastavka1.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN zastavka")
            currentstate = 2

        elif (komanda == 3 and currentstate != 3):
            print('play benz1')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/3.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU 3")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/3.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN 3")
            currentstate = 3

        elif (komanda == 4 and currentstate != 4):
            print('play benz2')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/4.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU 4")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/4.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN 4")
            currentstate = 4

        elif (komanda == 5 and currentstate != 5):
            print('play benz3')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/5.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU 5")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/5.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN 5")
            currentstate = 5

        elif (komanda == 6 and currentstate != 6):
            print('play vib pistolet i vstavte v bak')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/6.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU 6")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/6.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN 6")
            currentstate = 6

        elif (komanda == 7 and currentstate != 7):
            print('play vib pistolet i vstavte v bak')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/zastavka2.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU 7")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/zastavka2.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN 7")
            currentstate = 7

        elif (komanda == 8 and currentstate != 8):
            print('play vib pistolet i vstavte v bak')
            os.system('killall omxplayer.bin')
            sleep(0.5)
            if (languageState == 0):
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/zastavka3.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("RU 8")
            else:
                player=subprocess.Popen(['omxplayer','-b','--no-osd','--loop','/home/pi/en/zastavka3.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
                print("EN 8")
            currentstate = 8


b = threading.Thread(name='PlayerStart', target=PlayerStart)
f = threading.Thread(name='ButtonPressed', target=ButtonPressed)

f.start()
b.start()

try:
    root.mainloop()

except KeyboardInterrupt:
    sys.exit(0)
