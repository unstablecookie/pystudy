# Author - patreon.com/oleg_molchanov

import socket

from select import select

host = '127.0.0.1'
port = 5003

monitor = []

srvsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
srvsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
srvsocket.bind((host,port))
srvsocket.listen()

def srvfunc(srvsocket):
	print("waiting for connect...")
	csocket1, addr = srvsocket.accept()
	print('you are connected! : ip-> ', addr)
	monitor.append(csocket1)

def reply(csocket1):
	data1 = csocket1.recv(4096)
	if data1:
		msg = "responce message".encode()
		csocket1.sendall(msg)
	else:
		csocket1.close()


def loop():
	while True:
		ready, _, _ = select(monitor,[],[])
		for s in ready:
			if s is srvsocket:
				srvfunc(s)
			else:
				reply(s)

if __name__ == "__main__":
	monitor.append(srvsocket)
	loop()