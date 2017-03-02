import psutil
import time
import sys
import serial

#check to make sure there is an argument passed
args = sys.argv
if len(args) > 1:
	#TODO - connect to the serial port to pass information to the arduino
	arduino = serial.Serial(args[1], 9600)
	while True:
		cpuPercent = psutil.cpu_percent(interval=1)
		memory = psutil.virtual_memory()
		hard_drive = psutil.disk_usage('/')

		#TODO - send information to arduino
		print cpuPercent
		print memory.percent
		print hard_drive.percent
		time.sleep(5)
else:
	print "Please pass the serial port connected to arduino"