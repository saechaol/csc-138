# assignment.md

## Web Server Socket Programming in Python

### A brief rundown:
The goal of this lab is to provide a hands-on approach to socket programming for TCP connections in Python. In completing this assignment, I will demonstrate a proficiency in:
  * the creation of a server socket
  * binding the server socket to an address and port
  * sending and receiving HTTP packets
  * basics of the HTTP header format

The web server should support:
  * Handling HTTP requests at least one at a time
  * Acceptance and parsing of a given request
  * Obtaining a requested file from the server
  * Creating an HTTP response message of the requested file preceded by header lines
  * Sending an appropriate response directly to a client
  * Handling 404s

### Running the server:
An HTML file should exist within the same directory as the server. It can be reached via the host's IP address and port with an HTTP request.

### Self-Imposed Challenges
As it currently stands, the assignment specifies that the web server support extremely basic functionality. The following challenges are intended to improve my understanding of socket programming:
  * Implement a server that is able to handle multiple requests at the same time using multiple threads
  * Write an UNIX command-line HTTP client to connect to the server using a TCP connection. This client should support: creating a socket connection, sending a GET request, and displaying the server response