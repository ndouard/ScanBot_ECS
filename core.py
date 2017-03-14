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

import configparser
import os
import os.path
import sys
import pathlib
import time
import threading
from ftplib import FTP

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
	#bind pwm in @arduino via nanpy (knomb) to turret rot
	#bind 2/3-pos switch to tilt via nanpy
	#bind 2-pos switch to capture start/stop + delay writz via console
	try:
		capture.prepare_and_run_capture()
		turret = Turret()
		print("Press Ctrl+C to stop...")
		while(turret_active):
			turret.write_pwm_pan(radio.get_knob_level())
			turret.write_pwm_tilt(radio.get_3_pos_level())
			if radio.get_2_pos_level() >= 100:
				turret_active = false
		manual_stop()
		main()
	except KeyboardInterrupt:
		manual_stop()
		main()

def manual_stop():
	print('Stopping manual capture...')
	#stop actual capture
	#reset turret pos
	
def autonomous():
	print('Starting autonomous mode...')
	return


def autonomous_stop():
	return

def main():
#	try:
	selected_mode = get_user_command()
	selected_mode_name = str()
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
	main()

