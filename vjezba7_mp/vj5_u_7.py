from multiprocessing import pool
import socket
import sys
from datetime import datetime
import multiprocessing


def port_scanner(arg):
    remoteServerIP, PortNumber = arg
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.settimeout(0.5)
    result = tcp_sock.connect_ex((remoteServerIP, PortNumber))
    if result == 0:
        return PortNumber, True
    else:
        return PortNumber, False
    tcp_sock.close()


def pool_handler(ports):
    broj_cpu = multiprocessing.cpu_count()
    #print("Broj cvorova u ovom racunalu je %d "), "a koristiti cemo %d procesa" % (broj_cpu, broj_cpu*2)
    pool = multiprocessing.Pool(processes=broj_cpu*2)

    for port, status in pool.map(port_scanner, [(remoteServerIP, port) for port in ports]):

        #print("Skeniram port: %d") % port
        if status == True:
            #print("Port %d je otvoren") % port
            print("Port {}:           OOOOtvorenOOOO".format(port))
        else:
            print("Port {}:           Zatvoren".format(port))


if __name__ == "__main__":

    # remoteServer = input("Molim vas unesite adresu hosta koju zelite testirati: ")
    remoteServer = "www.google.hr"
    remoteServerIP = socket.gethostbyname(remoteServer)

    # socket.settimeout(0.5)

    print("-" * 60)
    print("Skeniram host: ", remoteServerIP)
    print("-" * 60)

    # port1 = int(input("Unesite prvi port: "))
    # port2 = int(input("Unesite drugi port: "))
    port1 = 80
    port2 = 90
    t1 = datetime.now()

    ports = range(port1, port2 + 1)

    pool_handler(ports)

    t2 = datetime.now()

    total = t2 - t1

    print("Skeniranje zavrseno za: ", total)
