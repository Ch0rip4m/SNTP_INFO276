import struct as stc
import ntplib as ntpl
import socket as skt
import time

TIME1970 = 2208988800  #tiempo trasncurrido desde el 01/01/1970

ntp = ntpl.NTPClient()

PORT = 8888
sock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
sock.bind(('',PORT))

print('CONEXIÓN UDP ESTABLECIDA...')

while True:
    data, clientAdress = sock.recvfrom(1024)

    solicitud = ntp.request('2.cl.pool.ntp.org')
    tiempo = solicitud.tx_time
    data = solicitud.to_data()
    data_bytes = bytearray(data)
    new_time_data = stc.pack('!1I', TIME1970 + int(tiempo))
    new_time_data_bytes = bytearray(new_time_data)
    data_bytes[40:43] = new_time_data_bytes
    
    solicitud.from_data(data_bytes)
    
    print('Tiempo: {}'.format(time.ctime(tiempo)))

    sock.sendto(data_bytes,clientAdress)