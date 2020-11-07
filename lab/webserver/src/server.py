# saechaol

# Specified requirements:
#  - handle http requests at least one at a time
#  - accept and parse http requests
#  - obtain the requested file from the web server
#  - create and send http response
#  - handle 404 file not found responses

# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# prepare server socket

# --start



# --end

while True:
	# establish connection
	print 'Ready to serve...'

	# connectionSocket, addr = --start --end

	try:
		# message = --start --end
		filename = message.split()[1]
		
		f = open(filename[1:])

		# outputdata = --start --end

		# send one http header line into socket

		# --start

		# --end

		# send the content of the requested file to the client
		for i in range(o, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		# send 404 response
		# --start

		# --end

		#close client socket
		# --start

		# --end
serverSocket.close()

