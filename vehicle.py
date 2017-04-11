import configparser
import os
import os.path
import sys
import pathlib
import time
import threading
from ftplib import FTP

import paramiko
	
def start_client(ip, username, password):
	final_command = 'bash /home/pi/ScanBot_ECS/navio_client/startup.sh'
	print('Start command: ' + final_command)
	
	#try:
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username=username, password=password)
	
	final_command = 'while true; do ' + final_command + ' && break; done'
	print('Will run: ' + final_command)
	print('Will now attempt to start vehicle data client...')
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(final_command)
	
	#except:
	#sys.exit('Could not start capture over SSH.')
	
