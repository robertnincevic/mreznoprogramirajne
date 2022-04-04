import socket
import subprocess
import sys
from datetime import datetime

remoteServer = raw_input("Upisi host name: ")
remoteServerIP = socket.gethostbyname(remoteServer)
# www.google.hr

port1 = int(raw_input("Upisi port1: "))
port2 = int(raw_input("Upisi port2: "))

print(port1,port2)
#print "Port {}:        Open".format(port2)

t1 = datetime.now()

try:
	for port in range (port1, port2):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result ==0:
			print ("Port {}:        Open".format(port))
			sock.close()

except KeyboardInterrupt:
	print "You pressed Ctrl+C"
	sys.exit()

except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()

t2 = datetime.now()


total = t2 - t1


print 'Scanning Completed in in ', total