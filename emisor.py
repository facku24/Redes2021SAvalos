#!/usr/bin/env python
# encoding: utf-8
"""
emisor.py
"""
from constantes import *
from socket import *
from paquete import *


# creamos el socket UDP
sender = socket(AF_INET, SOCK_DGRAM)
# ligamos la direccion
sender.bind((EMISOR_IP, EMISOR_PORT))

timer = TIMEOUT
sequence = SECUENCE_INIT % 2

send_to = None
received_from = (RECEPTOR_IP, RECEPTOR_PORT)

while (True):
	# mandar un paquete

	pckt = Paquete(EMISOR_PORT, RECEPTOR_PORT, 'mensaje numero ' + str(i), 0)
	# creo el mensaje a enviar
	destinatario = (RECEPTOR_IP, RECEPTOR_PORT)
	msj = dumps((destinatario, pckt))

	# envio a la red
	sender.sendto(msj, (NETWORK_IP, NETWORK_PORT))

sender.close()