import smbus
import time

bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
  bus.write_byte(address, value)
  return -1

def readNumber():
  number = bus.read_byte(address)
  return number

while True:
  var = int(input("Enter 1  ^ ^  9: "))
  if not var:
      continue

  writeNumber(var)
  print("RPI: Hi Arduino, I sent you ", var)
  # sleep one second for debug
  time.sleep(1)

  number = readNumber()
  print("Arduino: Hey RPI, I received a digit ", number)
  print()