import socket

try:
	print("Starting server...")
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind(('', 15555))
	print("Sever started")
	while True:
			socket.listen(5)
			client, address = socket.accept()
			print("{} connected".format( address ))

			response = client.recv(255)
			if response != "":
					radio_knob_level = response

	print("Close")
	client.close()
	stock.close()
except:
	print('Couldn\'t run server on master board. Is networking properly configured?')

	
