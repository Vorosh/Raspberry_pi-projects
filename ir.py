import os
import glob
import subprocess
from time import sleep
import lirc

sockid=lirc.init('ir',blocking = False)

st=0
flag=1

while True:
	if flag==1:
		player=subprocess.Popen(['omxplayer','-b','--loop','--no-osd','/home/pi/1.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
		fi=player.poll()
		flag=0
			
	code=lirc.nextcode()
	if code!=[]:
		if code[0]=="on":
			os.system('killall omxplayer.bin')
			player=subprocess.Popen(['omxplayer','-b','--no-osd','/home/pi/2.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
			fi=player.poll()
			st=0
		if code[0]=="off":
			os.system('killall omxplayer.bin')
			flag=1
		
	else:
		fi=player.poll()
		if (st==0 and fi==0):
			flag=1
		sleep(0.1)								
