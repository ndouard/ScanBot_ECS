import configparser
import os
import os.path
import sys
import pathlib
import time
import threading
from ftplib import FTP

class Turret:
	#see diagrams
	#from nanpy import Servo
	#servo_rotation = Servo(10)
	#servo_tilt = Servo(11)
	
	turret_count = 0
	
	def parse_turret_config(self):
		path = pathlib.Path('scanbot.cfg')
		if path.is_file():
			print("Reading turret config file...")
			config = configparser.ConfigParser()
			config.read('scanbot.cfg')
			tilt_servo_min = config['TURRET']['Tilt Servo Min']
			tilt_servo_max = config['TURRET']['Tilt Servo Max']
			tilt_servo_mid = config['TURRET']['Tilt Servo Mid']
			pan_servo_min = config['TURRET']['Pan Servo Min']
			pan_servo_max = config['TURRET']['Pan Servo Max']
			pan_servo_mid = config['TURRET']['Pan Servo Mid']
			
		else:
			print("Couldn't find turret config file. Creating a new one...")
			
			config = configparser.RawConfigParser()
			config['LOGGER'] = {}
			config['LOGGER']['IP'] = '192.168.1.1'
			config['LOGGER']['Username'] = 'Username'
			config['LOGGER']['Password'] = 'Password'
			config['LOGGER']['SSH Run Command'] = './Logger'
			
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
			
		print("Parsed the following data:")
		print("Tilt Servo Min: " + tilt_servo_min)
		print("Tilt Servo Max: " + tilt_servo_max)
		print("Tilt Servo Mid: " + tilt_servo_mid)
		print("Pan Servo Min: " + pan_servo_min)
		print("Pan Servo Max: " + pan_servo_max)
		print("Pan Servo Mid: " + pan_servo_mid)
		
		return [tilt_servo_min, tilt_servo_max, tilt_servo_mid, pan_servo_min, pan_servo_max, pan_servo_mid]
	
	def __init__(self):
		Turret.turret_count += 1
		self.parse_turret_config()
	
	def left90(self):
		#servo_tile.write()
		#servo_left.write()
		return
		
	def right90(self):
		#servo_tile.write()
		#servo_left.write()
		return

	def left180(self):
		#servo_tile.write()
		#servo_left.write()
		return

	def right180(self):
		#servo_tile.write()
		#servo_left.write()
		return

	def left(self):
		return

	def right(self):
		return

	def servo_demo(self):
		for move in [0, 90, 180, 90, 0]:
			servo_tilt.write(move)
			time.sleep(1)
		
		for move in [0, 90, 180, 90, 0]:
			servo_rotation.write(move)
			time.sleep(1)

	def write_pwm_pan(self, pwm_input):
		#coef + write servo_demo
		return

	def write_pwm_tilt(self, pwm_input):
		if pwm_input == 100:
			self.left()
		elif pwm_input == 200:
			self.right()
		else:
			print("Bad 3-pos PWM input - is the radio controller correctly configured?")

	def home():
		#go to default pos
		return


		
		
		
