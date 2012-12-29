#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com
import spidev
import time
import os
import RPi.GPIO as GPIO
import smbus

spi = spidev.SpiDev()
GPIO.setwarnings(False)

class Arduino:
    def __init__(self,mode):
        if mode == 'BCM':
            GPIO.setmode(GPIO.BCM)

    def pinMode(self,port,type):
        """ Take "In" or "OUT" and use it to set the port type"""
        if type == "IN":
            GPIO.setup(port,GPIO.IN)
        elif type == "OUT":
            GPIO.setup(port,GPIO.OUT)
        else:
            print "pinMode -- Type Error, must use either 'INPUT' or 'OUTPUT'"
    def digitalWrite(self,port,state):
        """Turn a GPIO port on or off"""
        if state == 'HIGH':
            state = True
        if state == 'LOW':
            state = False
        GPIO.output(port,state)
    def digitalRead(self,port):
        """Read the state of a GPIO port and flip the results because of the GPIO wiring"""
        if not GPIO.input(port):
            return True
        else:
            return False

    def analogRead(self,port):
        """Read the given ADC port and preform the necessary shifting of bits"""
        spi.open(0,0)
        if (port > 7) or (port < 0):
            print 'analogRead -- Port Error, Must use a port between 0 and 7'
            return -1
        r = spi.xfer2([1,(8+port)<<4,0])
        value = ((r[1]&3) << 8) + r[2]
        spi.close()
        return value

    def movavg(self,list, length, value):
        """A function that smooths the results by averaging a list"""
        #Courtesy Wolf Paulus
        list.append(value)
        if length < len(list) :
            del list[0]
        sum=0
        for x in list[:] :
            sum+=x
        return sum / len(list)


