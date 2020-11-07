# saechaol

# Specified requirements:
#  - handle http requests at least one at a time
#  - accept and parse http requests
#  - obtain the requested file from the web server
#  - create and send http response
#  - handle 404 file not found responses

# import socket module
from socket import *


LOCAL_HOST = "127.0.0.1"
SERVER_PORT = 12000

# prepare server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind the port to this socket
serverSocket.bind((LOCAL_HOST, SERVER_PORT))

# set the port to listening mode
# the socket will then be ready to receive client connection requests
serverSocket.listen(1)

while True:
	# establish connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()

	try:
		message = connectionSocket.recv(2048)

		filename = message.split()[1].decode()

		f = open(filename[1:], "r")
		print("filename: {}".format(filename))

		outputdata = f.read()

		# send 200 ok response
		response = ("HTTP/1.1 200 OK\n"
					"Server: Python 3.8.3\n"
					"Content-Type: text/html; charset=utf-8\r\n\n")
		connectionSocket.send(response.encode())

		# send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])

		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except IOError:
		# send 404 response
		response = ("HTTP/1.1 404 Not Found\n"
					"Server: Python 3.8.3\n"
					"Content-Type: text/html; charset=utf-8\r\n\n")

		#close client socket
		connectionSocket.send(response.encode())
		connectionSocket.send("\r\n".enocde())
		connectionSocket.close()

serverSocket.close()

