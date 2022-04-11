from logging.handlers import TimedRotatingFileHandler
import socket
import subprocess
import sys
from datetime import datetime
import threading
# from queue import Queue
# from queue import *
from multiprocessing import Process, Queue

t1 = datetime.now()

print_lock = threading.Lock()
q = Queue(maxsize=0)


def threader():
    while True:
        port = q.get()
        tcp_scanner(port)


def main():
    for x in range(port1, port2):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    for port in range(port1, port2):
        q.put(port)

    q.join


# remoteServer = raw_input("Upisi host name: ")
remoteServer = "www.google.hr"
remoteServerIP = socket.gethostbyname(remoteServer)
# www.google.hr

#port1 = int(raw_input("Upisi port1: "))
#port2 = int(raw_input("Upisi port2: "))

port1 = 80
port2 = 82

# print(port1, port2)
# print "Port {}:        Open".format(port2)


def tcp_scanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:        Open".format(port))
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


# print 'Scanning Completed in in ', total
if __name__ == '__main__':
    t2 = datetime.now()
    total = t2 - t1
    for port in range(port1, port2):
        tcp_scanner(port)
        print(total)
