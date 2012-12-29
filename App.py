#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

from Adafruit_LEDBackpack.Adafruit_7Segment import SevenSegment
from Ard import *

green = 25
yellow = 24
red = 23
mosfet = 18
led1 = 4
led2 = 22
led3 = 21
pot_adc = 7
light_adc = 6

mode = 0
l = list()
segment = SevenSegment(address=0x70) #which port the display is
A = Arduino("BCM") #define the port name style
print "Press CTRL+Z to exit"
#Set the port types
A.pinMode(green,'IN')
A.pinMode(yellow,'IN')
A.pinMode(red,'IN')
A.pinMode(led1,'OUT')
A.pinMode(led2,'OUT')
A.pinMode(led3,'OUT')

#Turn off all LEDs
A.digitalWrite(led1,"LOW")
A.digitalWrite(led2,"LOW")
A.digitalWrite(led3,"LOW")

while True:
    A.digitalWrite(led1,"HIGH")
    pot = A.analogRead(pot_adc)
    light = A.analogRead(light_adc)
    lightAvg = A.movavg(l,4,light)
    if A.digitalRead(green):
        mode = 0
    elif A.digitalRead(yellow):
        mode = 1
    elif A.digitalRead(red):
        A.digitalWrite(led1,"LOW")
        A.digitalWrite(led2,"LOW")
        A.digitalWrite(led3,"LOW")
        print 'App Terminated by RED BUTTON!'
        segment.writeInt(0000)
        break

    if not mode:
        A.digitalWrite(led2,"HIGH")
        A.digitalWrite(led3,"LOW")
        segment.writeInt(pot)
    elif mode:
        A.digitalWrite(led2,"LOW")
        A.digitalWrite(led3,"HIGH")
        segment.writeInt(lightAvg)

    time.sleep(.125)
    A.digitalWrite(led1,"LOW")
    time.sleep(.175)

