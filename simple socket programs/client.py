# Echo client program
import socket

HOST = ''    # The remote host
PORT = 8000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
message = raw_input("enter the message here")
s.send(message)
data = s.recv(1024)
s.close()
print 'Received', repr(data)

