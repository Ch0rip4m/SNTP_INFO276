#CLIENTE SNTP
import socket as skt
import time
from ntplib import NTPStats

stats = NTPStats()

HOST = "localhost"
PORT = 8888

sock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

i = 0
while i<10: 
    data = "Hello there"
    sock.sendto(data.encode(), (HOST, PORT))
    data = sock.recv(1024)

    stats.from_data(data)
    print('TIEMPO RECIBIDO: {}'.format(time.ctime(stats.tx_time)))
    time.sleep(3)
    i = i + 1