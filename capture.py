import configparser
import os
import os.path
import sys
import pathlib
import time
import threading
from ftplib import FTP

import paramiko

def parse_logger_info():
	pathRadser = pathlib.Path('scanbot.cfg')
	if pathRadser.is_file():
		print("Reading server info file...")
		config = configparser.ConfigParser()
		config.read('scanbot.cfg')
		ip = config['LOGGER']['IP']
		username = config['LOGGER']['Username']
		password = config['LOGGER']['Password']
		ssh_run_command = config['LOGGER']['SSH Run Command']
		
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
		
	print("Parsed the following data:")
	print("IP: " + ip)
	print("Username: " + username)
	print("Password: " + password)
	
	return [ip, username, password, ssh_run_command]

	
def start_logger_app(ip, username, password, ssh_run_command, duration, destination):
	final_command = ssh_run_command + ' --duration ' + duration + ' --destination \'' + destination + '\''
	print('Start command: ' + final_command)
	
	#try:
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username=username, password=password)
	
	final_command = 'while true; do ' + final_command + ' && break; done'
	print('Will run: ' + final_command)
	print('Will now attempt to start capture over SSH...')
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(final_command)
	
	#except:
	#sys.exit('Could not start capture over SSH.')
	
def prepare_and_run_capture(duration, destination):
	print("Current time is: " + time.ctime())
	serverConfig = parse_logger_info()	
	start_logger_app(serverConfig[0], serverConfig[1], serverConfig[2], serverConfig[3], duration, destination) #run app via SSH
	



