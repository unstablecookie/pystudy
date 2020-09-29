# simple network app. opens port on local server waiting for the input,
# send short message as response

import socket

host = '127.0.0.1'
port = 5002

# 'with' structure allows implicitly close the port .
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as socket1:
	socket1.bind((host,port))
	socket1.listen()
	csocket1, addr = socket1.accept()
	with csocket1:
		print('you are connected : ip-> ' , addr)
		while True:
			data1 = csocket1.recv(4096)
			if not data1:
				break
			msg = "simple network app".encode()
			csocket1.sendall(msg)