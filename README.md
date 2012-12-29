7-Seg-MCP3008
=============

Getting Starred with Raspberry Pi, Part 3 Example3

Connect the components as follows:
Component >> Connects to
Green Led	              >>    GPIO Port 22
Yellow Led              >>    GPIO Port 21
Red Led	                >>    GPIO Port 4
Potentiometer           >>    MCP3008 Port 7
Light Sensor/PhotoCell	>>    MCP3008 Port 6 and 3.3V
10K Resistor	          >>    PhotoCell and Ground
Green Button	          >>    GPIO Port 25
10K or More Resistor	  >>    Green Button and 3.3V
Yellow Button						>> 		GPIO Port 24
10K or More Resistor		>> 		Yellow Button and 3.3V
Red Button							>> 		GPIO Port 23
10K or More Resistor		>> 		Red Button and 3.3V
7-Segment								>> 		5V, Ground, SCL, SDA
MCP3008									>> 		Same Connections as in Example 2
