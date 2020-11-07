# threaded-server.py
# saechaol

# Challenge requirements:
#  	- implement a server capable of handling multiple simultaneous requests

# Implementation details:
# 	- To complete

# import socket module
from socket import *

# import cli argument parser module
from argparse import *

# import multi-threading module
from threading import *

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12000

# initialize parser
cliParser = ArgumentParser(description='Multithreaded CLI HTTP parser')

# add arguments
cliParser.add_argument(	'ip',
						nargs='?',
						default=SERVER_HOST,
						help='This is the name of the host to listen to. By default, it will attempt to listen on the localhost. ')

cliParser.add_argument( 'port',
						nargs='?',
						type=int,
						default=SERVER_PORT,
						help='This is the host\'s port to bind. By default, it will attempt to bind to port 12000. ')

# store arguments
args = cliParser.parse_args()

# create a welcoming TCP socket over IPV4
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind the port to this socket
serverSocket.bind((args.ip, args.port))

# set the socket into listening mode
# queue up to five requests rather than one
serverSocket.listen(5)

# establish connection
print('Listening on {}:{}! Ready to serve...'.format(args.ip, args.port))

def server(connectionSocket, addr):
	print('\nConnection request received from: {}'.format(addr))

	try:
		messages = connectionSocket.recv(2048)
		message = messages.decode().split('\r\n')[0]

		filename = message.split()[1]
		f = open(filename[1:], 'r')
		print('filename: {}'.format(filename))

		outputdata = f.read()

		# send 200 OK response
		response = ('HTTP/1.1 200 OK\n'
					'Server: Python 3.8.3\n'
					'Content-Type: text/html; charset=utf-8\r\n\n')
		connectionSocket.send(response.encode())

		# send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())

		connectionSocket.send('\r\n'.encode())
		connectionSocket.close()

	except IOError:
		# send 404 response
		response = ('HTTP/1.1 404 Not Found\n'
					'Server: Python 3.8.3\n'
					'Content-Type: text/html; charset=utf-8\r\n\n')

		# close client socket
		connectionSocket.send(response.encode())
		connectionSocket.send('\r\n'.encode())
		connectionSocket.close()

while True:
	connectionSocket, addr = serverSocket.accept()
	Thread( target=server,
			args=(connectionSocket, addr)).start()

