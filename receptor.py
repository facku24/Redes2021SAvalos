from constantes import *
from socket import *
from paquete import *

# Creo un socket UDP
receiver = socket(AF_INET, SOCK_DGRAM)
# Le asigno las direcciones IP y de Puerto
receiver.bind((RECEPTOR_IP, RECEPTOR_PORT))

send_to = (EMISOR_IP, EMISOR_PORT)

print("Server running and ready to receive data...\n")

while (True):
	# recibo el mensaje
	incoming_message, network_received_from = receiver.recvfrom(LONGITUD_UDP)
	received_from, package = loads(incoming_message)
	incoming_message = package.datos

	if calculo_checksum(package) == 0:
		new_data = package.datos.upper()
	else:
		new_data = ""

	if calculo_checksum(package) == 0:
		expected_sec = (package.secuencia + 1) % 2
	else:
		expected_sec = package.secuencia

	ACK_message = Paquete(RECEPTOR_PORT, EMISOR_PORT, new_data, expected_sec)
	message_to_send = dumps((send_to, ACK_message))
	receiver.sendto(message_to_send, (NETWORK_IP, NETWORK_PORT))
