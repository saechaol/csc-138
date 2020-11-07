# ToyTCPClient.py

# import socket library
from socket import *

# specify localhost and port
serverName = 'localhost'
serverPort = 12000

# create TCP socket for server
clientSocket = socket(AF_INET, SOCK_STREAM)

# for TCP connections, the client needs to first connect to the server
clientSocket.connect((serverName, serverPort))

# by this point, all handshaking should have occured
sentence = raw_input('Input lowercase sentence: ')

# unlike UDP connections, since we've established a connection, 
# .send() does not require a destination address or a port
clientSocket.send(sentence.encode())

# retrieves the reply message from the server as a string
modifiedSentence = clientSocket.recv(1024)

# prints the message
print('From Server:', modifiedSentence.decode())

# close the socket
clientSocket.close()