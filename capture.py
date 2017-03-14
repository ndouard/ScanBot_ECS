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
		print("Couldn't find server info file. Creating a new one...")
		
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
	print("IP: " + ip)
	print("Username: " + username)
	print("Password: " + password)
	
	return [ip, username, password, ssh_run_command]
	
def upload_capture_duration(ip, username, password):
	print("Attempting to connect to server...")
	print("IP: " + ip)
	print("Username: " + username)
	print("Password: " + password)
	try:
		connect = FTP(ip,username,password) #connect to server
		print("The server said: " + str(connect.getwelcome()))
		print("The server contains:")
		root = connect.dir()
		print(root)
	except:
		sys.exit("Could not connect to the server properly. Is the Minnowboard on?")
	
	#connect.sendcmd('CWD '+directory_name) change dir	


	print("Attempting to send capture delay file...")
	try:
		file = open('capture.cfg', 'rb')
		print('File is defined as: ' + str(file))
		connect.storbinary('STOR capture.cfg', file)
		file.close()
		connect.quit()
	except:
		sys.exit("An error occured and the file couldn't be sent to the server. Is the server correctly configured?")
	print("Scheduled upload tasks done.")

def start_logger_app(ip, username, password, ssh_run_command):
	print('Will now attempt to start capture over SSH...')
	# try:
		# ssh = paramiko.SSHClient()
		# ssh.connect(ip, username=username, password=password)
		# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_run_command)
	# except:
		# sys.exit('Could not start capture over SSH.')
	
def prepare_and_run_capture():
	print("Current time is: " + time.ctime())
	print("Server upload program starting...")
	#serverConfig array contains ip, username, password
	serverConfig = parse_logger_info()
	upload_capture_duration(serverConfig[0], serverConfig[1], serverConfig[2])
	start_logger_app(serverConfig[0], serverConfig[1], serverConfig[2], serverConfig[3])


