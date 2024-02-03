# #!/usr/bin/env python
# import os
# import glob
# import time
# import datetime
# import max7219.led as led
# from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
# from random import randrange
# import RPi.GPIO as GPIO
# import threading
# from threading import Thread

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(21, GPIO.IN)
# GPIO.setup(26, GPIO.OUT)

# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')

# base_dir = '/sys/bus/w1/devices/'
# device_folder = glob.glob(base_dir + '28*')[0]
# device_file = device_folder + '/w1_slave'

# def read_temp_raw():
# 	f = open(device_file, 'r')
# 	lines = f.readlines()
# 	f.close()
# 	return lines
	
# def read_temp():
# 	lines = read_temp_raw()
# 	while lines[0].strip()[-3:] != 'YES':
# 		time.sleep(0.2)
# 		lines = read_temp_raw()
# 	equals_pos = lines[1].find('t=')
# 	if equals_pos != -1:
# 			temp_string = lines[1][equals_pos+2:]
# 			temp_c = float(temp_string) / 1000.0
# 			temp_f = temp_c * 9.0 / 5.0 + 32.0
# 	return temp_c#,temp_f  #Remove # if temperature requirement is in Fahrenheit
			
# def fuc2():		
# 	while True:
# 			print('C T is ',str("%.2f" % read_temp())+ "`C")
# 			a=input("Enter the temperature value between 24 & 30: ")
# 			if a>=24 and a<=30:
# 				print("Good to go")
# 				break
# 			else:
# 				print("Wrong Input")
# 			continue	
	
# 	while True:
# 		if read_temp() >= a:
# 			GPIO.output(26,1)
# 		elif read_temp() <= a-2:
# 			GPIO.output(26,0)
	
			
# def fuc1():		
# 	while True: 
# 		device = led.matrix(cascaded=1)
# 		rd=read_temp()
# 		con = str("%.2f" % rd)+"`C" 			#+"Time is "+str(datetime.datetime.now().time()) "%.2f" %" for TWO decimial point
# #		print(con) #To display on the terminal
# #		print(datetime.datetime.now().time())
# 		device.show_message(con, font=proportional(CP437_FONT))
		
		
# Thread(target=fuc1).start()
# Thread(target=fuc2).start()

print("Wrong Input")
