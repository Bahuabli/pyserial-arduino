"""
giving commends to arduino through text file 

this python program will send commands to arduino board 
through serial port

Author : Bahubali Fuladi
"""

import serial		#library for serial port
import time		#library for delay

myfile = open('inputfile','r')		#opening the input file
"""
these set of function will give command to arduino connected on serial port 
"""

def servoWrite(angle):			#function for writing servo motor angle
	if angle> 0 and angle <180:
		ser.write("C")
		b = chr(angle)
		ser.write(b)
		print 'servo ',angle
	else:
		print "Servo Angle is out of range"


def ledON():			#function for switching LED ON
	ser.write("A")
	print 'LED ON'

def ledOFF():			#function for switching LED OFF
	ser.write("B")
	print 'LED OFF'


def potWrite(value):		#function for writing resistor value on digital pot connected on arduing 
	if value> 0 and value <180:		#over SPI
		ser.write("D")
		b = chr(value)
		ser.write(b)
		print 'POT ',value
	else:
		print "POT value is out of range"

ser = serial.Serial('/dev/ttyUSB0')	#creating serial port object
ser.baudrate = 9600			#seting baud rate of serial communication
print(ser.name)				#print name of serial port 
time.sleep(1)				#this delay will allow arduino to boot up and make it ready to get commends 

for line in myfile:			#loop for reading file line by line
	line = line.strip()
	line = line.upper()		
	if line.startswith('DELAY'):			#check for delay command in line
#		print line
		time.sleep(float(line.split()[1]))	#call delay sub
	elif line.startswith('LED'):			#check for LED command in line
		if line.split()[1] == 'ON':		#switching LED ON or OFF
			ledON()
		if line.split()[1] == 'OFF':
			ledOFF()
#		print line
	elif line.startswith('SERVO'):			#check for servo commend in line
		servoWrite(int(line.split()[1]))
	elif line.startswith('POT'):			#check for pot command in line
		potWrite(int(line.split()[1]))
		

ser.close()	#close the serial port 
