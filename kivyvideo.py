import kivy
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import os
import subprocess
import glob
from time import sleep
from kivy.animation import Animation
from kivy.uix.scatter import ScatterPlane
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
import kivy.core.window
from random import randint
from functools import partial

import RPi.GPIO as GPIO


# Set up GPIO:
buttonPin1 = 23
buttonPin = 14
buttonPin2 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Modify the Button Class to update according to GPIO input:
class InputButton(Button):
	def update(self, dt):
		if GPIO.input(buttonPin) == False:
			self.state = 'normal'
			sleep(1.5)
			player=subprocess.Popen(['omxplayer','-b','--no-osd','/home/pi/videos/loop1.mp4'],stdin=subprocess.PIPE)#,stdout=subprocess.PIPE,stderr=subprocess.PIPE
		else:
			self.state = 'down'			

class InputButton1(Button):
	def update(self, dt):
		if GPIO.input(buttonPin1) == False:
			self.state = 'normal'
		else:
			self.state = 'down'	

class InputButton2(Button):
	def update(self, dt):
		if GPIO.input(buttonPin2) == False:
			self.state = 'normal'
		else:
			self.state = 'down'	
			

class MyApp(App):
	def build(self):
		# Set up the layout:
		layout = GridLayout(cols=1, spacing=110, padding=150, row_default_height=100)

		# Make the background gray:
		with layout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(1920,1080), pos=layout.pos)

		# Instantiate the first UI object (the GPIO input indicator):
		inputDisplay = InputButton(text="Input")
		inputDisplay1 = InputButton1(text="Input1")
		inputDisplay2 = InputButton2(text="Input2")

		# Schedule the update of the state of the GPIO input button:
		Clock.schedule_interval(inputDisplay.update, 1.0/10.0)
		Clock.schedule_interval(inputDisplay1.update, 1.0/10.0)
		Clock.schedule_interval(inputDisplay2.update, 1.0/10.0)

		
		wimg = Image(source='logo.png')
		
		# Add the UI elements to the layout:
		layout.add_widget(wimg)
		layout.add_widget(inputDisplay)
		layout.add_widget(inputDisplay1)
		layout.add_widget(inputDisplay2)
		

		return layout

if __name__ == '__main__':
	MyApp().run()

