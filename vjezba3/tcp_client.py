#tcp_client.py

import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 9999

client_socket.connect((host,port))
print client_socket.recv(1024)
client_socket.close()

 # client_socket.connect((host,port)) --- pokušava se spojit na host koji je 
 # deklariran sa socket.gethostname(), ZNAČI DA DOHVAĆA HOST KOJI JE POKRENUT
 # PREKO PORTA 9999
 
 
 
 # kod ispisa „Got connection...“? - DRUGI BROJ ZNAČI BROJ PORTA
 #