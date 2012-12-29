#!/usr/bin/python

import time
import datetime
from Adafruit_LEDBackpack import LEDBackpack

# ===========================================================================
# 7-Segment Display
# ===========================================================================

# This class is meant to be used with the four-character, seven segment
# displays available from Adafruit

class SevenSegment:
    disp = None

    # Hexadecimal character lookup table (row 1 = 0..9, row 2 = A..F)
    digits = [ 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F,
               0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71 ]

    # Constructor
    def __init__(self, address=0x70, debug=False):
        if (debug):
            print "Initializing a new instance of LEDBackpack at 0x%02X" % address
        self.disp = LEDBackpack(address=address, debug=debug)

    def writeDigitRaw(self, charNumber, value):
        "Sets a digit using the raw 16-bit value"
        if (charNumber > 7):
            return
            # Set the appropriate digit
        self.disp.setBufferRow(charNumber, value)

    def writeDigit(self, charNumber, value, dot=False):
        "Sets a single decimal or hexademical value (0..9 and A..F)"
        if (charNumber > 7):
            return
        if (value > 0xF):
            return
            # Set the appropriate digit
        self.disp.setBufferRow(charNumber, self.digits[value] | (dot << 7))

    def setColon(self, state=True):
        "Enables or disables the colon character"
        # Warning: This function assumes that the colon is character '2',
        # which is the case on 4 char displays, but may need to be modified
        # if another display type is used
        if (state):
            self.disp.setBufferRow(2, 0xFFFF)
        else:
            self.disp.setBufferRow(2, 0)

    def writeInt(self, value):
        """
        Write The 'Value' to the display
        """
        if value >9999:
            #Maxed OUT!
            value = 9999
        else:
            value = int(value)

        self.writeDigit(0, (value/1000)%10)
        self.writeDigit(1, (value/100)%10)
        self.writeDigit(3, (value/10)%10)
        self.writeDigit(4, value%10)

    def writeNum(self,value):
        if value>999:
            self.writeInt(value)
        elif value>99:
            self.writeDigit(0, int(value/100))
            self.writeDigit(1, (value/10)%10)
            self.writeDigit(3, value%10, True) #Add Decimal
            self.writeDigit(4, (value*10)%10)
        elif value >9:
            self.writeDigit(0, int(value/10))
            self.writeDigit(1, value%10, True)
            self.writeDigit(3, (value*10)%10)
            self.writeDigit(4, (value*100%10))
        else:
            self.writeDigit(0, int(value*10), True)
            self.writeDigit(1, (value*100)%10)
            self.writeDigit(3, (value*1000)%10)
            self.writeDigit(4, (value*10000)%10)

