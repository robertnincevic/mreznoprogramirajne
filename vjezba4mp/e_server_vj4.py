#echo_server.py
import socket
import datetime
from zad1 import print_machine_info


print datetime.datetime.now()
print_machine_info()

host=socket.gethostname()
port=12345

echo_server=socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)

print "Cekam klijenta.."
conn, addr=echo_server.accept() # prihvacanje konekcije kada se klijent spoji
print "Spojen: ", addr

br=1
while br< 1000:

	data=conn.recv(1024)
	if not data: break
conn.sendall(data)
	
conn.close()

