import smbus
import time
import socket
import subprocess
import os
import glob
from time import sleep

bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

UDP_PORT = 5003
UDP_IP = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def writeNumber(value):
  bus.write_byte(address, value)
  return -1

def readNumber():
  number = bus.read_byte(address)
  return number

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode('utf-8')
    if not data:
        break
    print("" + data)
    if data == 'PLAY':
        writeNumber(1)
        print("RPI: Hi Arduino, I sent you ", 1)
        # sleep one second for debug
        time.sleep(1)
        number = readNumber()
        print("Arduino: Hey RPI, I received a digit ", number)
        player=subprocess.Popen(['mplayer','/home/pi/111.mp3'],stdin=subprocess.PIPE)
             
sock.close()