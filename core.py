from __future__ import print_function
'''
Handles instances
	Capture start/stop
	Turret high level commands
	Vehicle nav override

Handles processes
	Manual radio control capture using knob as turret orientation control and 3 pos 'mode' switch as +45, 0, -45 sensor horizontal angle command
	Autonomous scan: swipes room, handles start/stop automatically - possible to end capture manually

Core acts as a console program - leaves room for GUI implementation
'''

import sys
#handles low level turret actions

from Turret import Turret

#start/stop capture - handles Minnowboard dialog
import capture
import radio
import vehicle

import configparser
import os
import os.path
import sys
import pathlib
import time
import threading
from ftplib import FTP

import socket

def get_user_command():
	print('Possible capture modes:')
	print('#1 - Manual')
	print('#2 - Autonomous')
	print('Other:')
	print('#3 - Quit')
	print('What will you choose? (1/2/3)')
	user_input = input()
	#need to parse properly!
	selected_mode = int(user_input)
	return selected_mode

def manual():
	print('Starting manual mode...')
	turret_active = True
	#bind pwm in @arduino via nanpy (knob) to turret rot
	#bind 2/3-pos switch to tilt via nanpy
	#bind 2-pos switch to capture start/stop + delay writz via console
	try:
		#delay is stored in capture.cfg - could add user prompt for auto file write later
		duration = input('How long do you want capture to run (seconds)? ')
		name = input('What name do you want for your KLG file? ')
		
		destination = '/home/logger/logs/' + name + '.klg'
		print('Destination is: ' + destination)
		
		#mandatory:
		capture.prepare_and_run_capture(duration, destination)
		turret = Turret()
		
		#start client
		print('Starting client...')
		vehicle.start_client('192.168.0.102', 'pi', 'aqw743zsx')
		
		#listening for radio_knob_level update
		print('Starting server for' + duration + 'seconds...')
		socket.listen(5)
		client, address = socket.accept()
		print("{} connected".format( address ))
		
		print("Press Ctrl+C to stop...")
		
		last_pwm_input = int(787/2)
		max_time = time.time() + duration
		while(turret_active):
			
			response = client.recv(255)
			if response != "":
					#print(response)
					radio_knob_level = int(response)
			
			#execute command after data fetch
			turret.write_pwm_pan(radio_knob_level, last_pwm_input)
			turret.write_pwm_tilt(radio.get_3_pos_level())
			last_pwm_input = radio_knob_level
			if radio.get_2_pos_level() >= 100:
				turret_active = False
			elif time.time() > max_time:
				turret_active = False
		print("Closing server connection...")
		client.close()
		stock.close()
		manual_stop()
		main()
	except KeyboardInterrupt:
		sys.exit("The program will now stop.")

def manual_stop():
	
	print('Stopping manual capture...')
	#stop actual capture
	#reset turret pos
	
def autonomous():
	print('Starting autonomous mode...')
	return


def autonomous_stop():
	return

def check_config():
	path = pathlib.Path('scanbot.cfg')
	if path.is_file():
		print("Read config OK...")	
	else:
		print("Couldn't find turret config file. Creating a new one...")
		
		config = configparser.RawConfigParser()
		config['LOGGER'] = {}
		config['LOGGER']['IP'] = '192.168.1.1'
		config['LOGGER']['Username'] = 'Username'
		config['LOGGER']['Password'] = 'Password'
		config['LOGGER']['SSH Run Command'] = './Logger'
		
		config['NAVIO'] = {}
		config['NAVIO']['IP'] = '192.168.1.1'
		config['NAVIO']['Username'] = 'Username'
		config['NAVIO']['Password'] = 'Password'
		config['NAVIO']['SSH Run Command'] = './Logger'
		
		config['TURRET'] = {}
		config['TURRET']['Tilt Servo Min'] = '0'
		config['TURRET']['Tilt Servo Max'] = '255'
		config['TURRET']['Tilt Servo Mid'] = '127'
		config['TURRET']['Pan Servo Min'] = '0'
		config['TURRET']['Pan Servo Max'] = '255'
		config['TURRET']['Pan Servo Mid'] = '127'
		
		
		with open('scanbot.cfg', 'w') as configfile:
			config.write(configfile)
		
		sys.exit("Please edit \"scanbot.cfg\" with correct information. The program will now stop.")
		
def main():
#	try:
	check_config()
	selected_mode = get_user_command()
	selected_mode_name = str("")
	if selected_mode == 1:
		selected_mode_name = 'Manual'
	elif selected_mode == 3:
		sys.exit("Closing application...")
	else:
		selected_mode_name = 'Autonomous'
	print('Mode #' + str(selected_mode) + ' - ' + selected_mode_name + ' will be used.')
	if selected_mode == 1:
		manual()
	else:
		autonomous()
#	except:
#		print('An unknown error occured and execution couldn\'t continue.')
#		try:
#			sys.exit(0)
#		except SystemExit:
#			os._exit(0)	

if __name__ == '__main__':
	print("Starting server...")
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind(('', 15555))
	print("Sever started")
	main()

