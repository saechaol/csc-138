# ToyTCPServer

# import socket library
from socket import *

# specify a port for this socket
serverPort = 12000

# create a welcoming TCP socket over IPV4
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind the port to this socket
serverSocket.bind(('', serverPort))

# set the socket into listening mode
# the socket is now ready to receive client connection requests
serverSocket.listen(1)

print 'The server is ready to receive messages'

while True:
	# connect to a client
	# this is where the server will wait until it receives a client connection 
	# when a connection is established, a NEW socket is created to communicate with the client
	# this socket is exists alongside the welcoming socket in line 10
	connectionSocket, clientAddress = serverSocket.accept()

	# reads bytes from the socket but not the address, unlike with UDP
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.uppder()

	# send message back to client with the connection socket
	connectionSocket.send(capitalizedSentence.encode())

	connectionSocket.close()