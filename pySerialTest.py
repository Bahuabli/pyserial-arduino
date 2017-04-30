import serial
import time
import re
myfile = open('inputfile','r')

def servoWrite(angle):
	if angle> 0 and angle <180:
		ser.write("C")
		b = chr(angle)
		ser.write(b)
		print 'servo ',angle
	else:
		print "Servo Angle is out of range"


def ledON():
	ser.write("A")
	print 'LED ON'

def ledOFF():
	ser.write("B")
	print 'LED OFF'


def potWrite(value):
	if value> 0 and value <180:
		ser.write("D")
		b = chr(value)
		ser.write(b)
		print 'POT ',value
	else:
		print "POT value is out of range"

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
print(ser.name)
time.sleep(1)

for line in myfile:
	line = line.upper()
	if line.startswith('DELAY'):
#		print line
		time.sleep(float(line.split()[1]))
	elif line.startswith('LED'):
		if line.split()[1] == 'ON':
			ledON()
		if line.split()[1] == 'OFF':
			ledOFF()
#		print line
	elif line.startswith('SERVO'):
		servoWrite(int(line.split()[1]))
	elif line.startswith('POT'):
		potWrite(int(line.split()[1]))
		




	

ser.close()
