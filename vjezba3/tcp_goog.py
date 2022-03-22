#tcp_client.py

import socket

client_socket = socket.socket()
host = socket.gethostbyname('www.google.com')
port = 80

client_socket.connect((host,port))
print ('Socket succesfu has successfully connected to Gogle on port = ' , port, ' and ip adress = ', host)
client_socket.close()

 