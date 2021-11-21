#!/usr/bin/env python
# encoding: utf-8
"""
emisor.py
"""
from constantes import *
from socket import *
from paquete import *
import select
from time import sleep


# creamos el socket UDP
sender = socket(AF_INET, SOCK_DGRAM)
# ligamos la direccion
sender.bind((EMISOR_IP, EMISOR_PORT))

timer = TIMEOUT
secuencia = SECUENCE_INIT % 2

send_to = None
received_from = (RECEPTOR_IP, RECEPTOR_PORT)

inputs = [sender]
outputs = [sender]
errors = []

while inputs:
	new_input, new_output, new_error = select.select(inputs,outputs,errors)

	if timer == 0:
		message = send_to
		sender.sendto(message, (NETWORK_IP, NETWORK_PORT))
		timer = TIMEOUT

	for in_signal in new_input:
		incoming_message, serverAddress = sender.recvfrom(LONGITUD_UDP)
		sended_from, incoming_package = loads(incoming_message)

		if incoming_package.secuencia == secuencia:
			message = send_to
			sender.sendto(message, (NETWORK_IP, NETWORK_PORT))
			timer = TIMEOUT
		else:
			print(package.datos)
			secuencia = incoming_package.secuencia
			send_to = None

	for output in outputs:
		if send_to == None or loads(send_to)[1].secuencia != secuencia:
			data = input('Input lowercase sentence: ')

			package = Paquete(EMISOR_PORT, RECEPTOR_PORT, data, secuencia)
			message = dumps((received_from, package))

			sender.sendto(message, (NETWORK_IP, NETWORK_PORT))
			send_to = message
			timer = TIMEOUT

		sleep(1)
		timer -= 1