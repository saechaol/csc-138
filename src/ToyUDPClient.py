from socket import * # includes python's socket library

serverName = 'localhost'
serverPort = 12000

# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get user input from screen
message = raw_input('Input lowercase sentence:')

# attach server name, port to message, and send into socket
clientSocket.sendto(message.encode(), (serverName, serverPort))

# retrieves the modified reply message from socket into a string
# returns the message, and the ip address of the message
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# prints message to the console
print modifiedMessage.decode()

# close the socket
clientSocket.close()