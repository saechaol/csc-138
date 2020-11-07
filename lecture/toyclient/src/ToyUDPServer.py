# import socket library
from socket import *

# specify port
serverPort = 12000

# create a UDP socket 
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind the socket to port 12000
serverSocket.bind(('', serverPort))

print("The server is ready to receive")
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)