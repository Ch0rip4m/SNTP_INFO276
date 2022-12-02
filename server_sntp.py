import struct as stc
import ntplib as ntpl
import socket as skt
import time

TIME1970 = 2208988800  #tiempo trasncurrido desde el 01/01/1970

ntp = ntpl.NTPClient() # inicializacion de ntplib

PORT = 8888
sock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM) #conexion UDP
sock.bind(('',PORT))

print('CONEXIÓN UDP ESTABLECIDA...')

while True:
    mensaje, clientAdress = sock.recvfrom(1024) # recepcion del mensaje y direccion del cliente

    solicitud = ntp.request('2.cl.pool.ntp.org')
    tiempoServidor = solicitud.tx_time #timestamp cliente
    mensaje = solicitud.to_data()
    msj_bytes = bytearray(mensaje) #codificacion para respuesta a cliente
    nuevoTiempo = stc.pack('!1I', TIME1970 + int(tiempoServidor)) 
    nuevoTiempo_bytes = bytearray(nuevoTiempo)
    msj_bytes[40:43] = nuevoTiempo_bytes
    
    solicitud.from_data(msj_bytes)
    
    print('TIEMPO SERVIDOR: {}'.format(time.ctime(tiempoServidor)))

    sock.sendto(msj_bytes,clientAdress)