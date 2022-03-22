#echo_client.py
import socket
import datetime

ime='robert_nincevic'

from zad1 import print_machine_info


print datetime.datetime.now()
print_machine_info()

host=socket.gethostname()
port=12345
client_socket=socket.socket()  # TCP SOCKET
client_socket.connect((host,port))
upit=raw_input('Ispisi text: ')

if(upit == ime):
	print("Taj unos nije podrzan")
	



client_socket.sendall(upit)
data = client_socket.recv(1024) # Tekst koji je pripremljen od servera

print data # ispis podataka
client_socket.close() # zatvaranje konekcije
