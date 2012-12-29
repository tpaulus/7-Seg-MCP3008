7-Seg-MCP3008
=============

Getting Starred with Raspberry Pi, Part 3 Example3

Connect the components as follows:
Component 				>> 	  Connects to,
Green Led	            >>    GPIO Port 22,
Yellow Led              >>    GPIO Port 21,
Red Led	                >>    GPIO Port 4,
Potentiometer           >>    MCP3008 Port 7,
Light Sensor/PhotoCell	>>    MCP3008 Port 6 and 3.3V,
10K Resistor	        >>    PhotoCell and Ground,
Green Button	        >>    GPIO Port 25,
10K or More Resistor	>>    Green Button and 3.3V,
Yellow Button			>> 	  GPIO Port 24,
10K or More Resistor	>> 	  Yellow Button and 3.3V,
Red Button				>> 	  GPIO Port 23,
10K or More Resistor	>> 	  Red Button and 3.3V,
7-Segment				>> 	  5V, Ground, SCL, SDA,
MCP3008					>> 	  Same Connections as in Example 2

Read the Value of the Pot or Light Reader, based on the Mode, which is determined by
buttons, and the red button kills the app.

Ard.py, is the resource library with all the simplified functions, and App, is the designated executable. Press the Green Button for the Pot value to be displayed, press the yellow button to display the light sensor reading. The red button kills the application.
The Red led blinks every time a reading is taken, the Yellow and Green leds indicate which mode the app is in, they match with the button colors.