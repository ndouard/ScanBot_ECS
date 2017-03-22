import socket
import sys, time

import navio.rcinput
import navio.util

#TODO: parse w/ cfg 
host = "192.168.43.208"
port = 15555

#try:
#navio defs
#navio.util.check_apm()
rcin = navio.rcinput.RCInput()

#open socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
print('Connection on {}'.format(port))

#TODO: set not running behavior 
running = True
while running:
	#read period
	#corresponds to Aux1 bound to RKnob
	period = str(rcin.read(5))
	print(period)
	#send period
	socket.sendall(bytes('cats', encoding="ascii"))
	time.sleep(1)
socket.close()
print("Closing socket...")
	
#except:
#	print('Cound not send data to master board server. Is networking properly configured?')