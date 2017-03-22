import socket
import sys, time

import navio.rcinput
import navio.util

#TODO: parse w/ cfg 
host = "localhost"
port = 15555

try:
	#navio defs
	navio.util.check_apm()
	rcin = navio.rcinput.RCInput()
	
	#open socket
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.connect((host, port))
	print('Connection on {}'.format(port))
	
	#TODO: set not running behavior 
	running = True
	while running:
		#read period
		period = rcin.read(2)
		#send period
		socket.sendall(bytes(period, encoding="ascii"))
		time.sleep(1)
	socket.close()
	print("Closing socket...")
	
except:
	print('Cound not send data to master board server. Is networking properly configured?')