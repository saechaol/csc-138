# Lucas Saechao
# CSC-138 Section 06
# 12/13/2020

from socket import *
from ssl import create_default_context
from base64 import b64encode
from getpass import getpass

HOSTNAME = "smtp.gmail.com"
PORT = 465

# u: mailclient13579@gmail.com
EMAIL = "mailclient13579@gmail.com"
PASSWORD = str(getpass(prompt = "Enter password for {}: ".format(EMAIL)))

TO = str(input("Enter receipient's email: "))
SUB = str(input("Enter subject: "))
MSG = str(input("Enter message: "))

ctx = create_default_context()

class Client:
	def __init__(self, socket):
		self.socket = socket

	def build_command(self, *args, size=1024, response=None):
		if args:
			build_command = args[0] + "\r\n"
			self.socket.send(build_command.encode())

		recv = self.socket.recv(size).decode()

		if response and recv[:3] != str(response):
			print(recv)
			print("{} reply not received from server".format(response))

with socket(AF_INET, SOCK_STREAM) as s:
	with ctx.wrap_socket(s, server_hostname=HOSTNAME) as s_socket:
		s_socket.connect((HOSTNAME, PORT))

		client = Client(s_socket)

		client.build_command(response=220)

		client.build_command("HELO {}".format(HOSTNAME), response=250)

		client.build_command("AUTH LOGIN", response=334)

		user = b64encode(EMAIL.encode()).decode()
		client.build_command(user, response=334)

		pw = b64encode(PASSWORD.encode()).decode()
		client.build_command(pw, response=235)

		client.build_command("MAIL FROM: <{}>".format(EMAIL), response=250)
		client.build_command("RCPT TO: <{}>".format(TO, response=250))
		client.build_command("DATA", response=354)

		message_frag_one 	= "From: <{}>\n".format(EMAIL)
		message_frag_two 	= "To: <{}>\n".format(TO)
		message_frag_three 	= "Subject: {}\n".format(SUB)
		message_frag_four	= "{}\n".format(MSG)
		message_end_frag 	= "\r\n."

		message = message_frag_one + message_frag_two + message_frag_three + message_frag_four + message_end_frag

		client.build_command(message, response=250)
		client.build_command("QUIT", response=221)

