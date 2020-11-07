# cli-client.py
# saechaol

# Challenge requirements:
#  	- implement a unix command-line http client to open a tcp socket connection
#  	- the client should be able to create a socket connection
#  	- the client should be able to send an HTTP GET request
#	- the client should be able to display the server response information

# Implementation details:
# 	- Client supports three arguments: hostname, port, file
#	
#   - If the client is run without arguments, it will attempt to request 
#		'helloworld.html' from 127.0.0.1 over port 12000. 
#
#	- python3 cli-client.py 127.0.0.1 12000 helloworld.html	 
#
#	- If it is able to retrieve the file, it will then print its contents
#		to the CLI display.

# import socket module
from socket import *

# import cli argument parser module
from argparse import *

# initialize parser
cliParser = ArgumentParser(description='CLI HTTP Client')

# add arguments
cliParser.add_argument(	'hostname',
						nargs='?',
						default='127.0.0.1',
						help='This is the name of the host to connect to. By default, it will attempt to connect to your localhost. ')

cliParser.add_argument( 'port',
						nargs='?',
						type=int,
						default='12000',
						help='This is the host\'s port to connect to. By default, it will attempt to connect over port 12000. ')

cliParser.add_argument( 'file',
						nargs='?',
						default='helloworld.html',
						help='This is the specific file to retrieve from the host. By default, it will attempt to retrieve helloworld.html. ')

# store arguments
args = cliParser.parse_args()

# create TCP socket for the server
clientSocket = socket(AF_INET, SOCK_STREAM)

# for TCP connections, the client needs to first connect to the server
print('Host: ' + args.hostname + '\nPort: ' + str(args.port) + '\nRequested file: ' + args.file)
clientSocket.connect((args.hostname, args.port))

# send an HTTP GET request and retrieve the specified file
request = 'GET /{} HTTP/1.1'.format(args.file)
clientSocket.sendall(request.encode('utf-8'))

response = ''
while True:
	responseData = clientSocket.recv(4096)
	if not responseData:
		break
	else:
		response += responseData.decode('utf-8')

print(response)

# close the socket
clientSocket.close()