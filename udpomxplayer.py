#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import socket
from time import sleep
import os
import glob
from threading import Lock, Thread
import threading
import subprocess
from tkinter import *
import sys

root = Tk()
root["bg"] = "black"
root.geometry("1920x1080")
root.attributes('-fullscreen', True)
root.config(cursor="none")
root.bind('<Escape>',lambda e: root.destroy())

flag=1
pt=0
st=0
tt=1
v1=0
v2=0
v3=0
komanda=0

UDP_PORT = 5003
UDP_IP = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))



def foreground():
    global data
    global komanda
    global v1
    global v2
    global v3
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            data = data.decode('utf-8')
            print('FOREGROUND')
            if tt==1:
                print("" + data)
                sleep(0.2)
                if (data == 'video1'):
                    if (komanda != 1):
                        print(komanda)
                        komanda = 1
                
                if (data == 'video2'):
                    if (komanda != 2):
                        komanda = 2
                
                if (data == 'video3'):
                    if (komanda != 3):
                        komanda = 3
            
            else:
                print('else foreground')
                
        except:
            print('excepppppt')
            sleep(2)
    
    sock.close()

def background():
    global flag
    global komanda
    global currentstate
    currentstate = 0
    while True:
        if flag==1:
            print('flag1')
            player=subprocess.Popen(['omxplayer','-b','--loop','--no-osd','/home/pi/Videos/7.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
            fi=player.poll()
            currentstate=0
            komanda=0
            flag=0
            st=0
            pt=0
        
        if (komanda == 1 and currentstate != 1):
            print('play1')
            os.system('killall omxplayer.bin')
            sleep(0.1)
            player=subprocess.Popen(['omxplayer','-b','--no-osd','/home/pi/Videos/2.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
            currentstate = 1
            
            
    
        elif (komanda == 2 and currentstate != 2):
            print('play2')
            os.system('killall omxplayer.bin')  
            sleep(0.1)
            player=subprocess.Popen(['omxplayer','-b','--no-osd','/home/pi/Videos/8.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
            currentstate = 2
            
            
    
        else:
            fi=player.poll()
            sleep(0.5)
            print("else")
            if(st==0 and fi==0):
                flag=1
    
    
b = threading.Thread(name='background', target=background)
f = threading.Thread(name='foreground', target=foreground)

b.start()
f.start()

try:
    root.mainloop()

except KeyboardInterrupt:
    sys.exit(0)
