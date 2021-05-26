from socket import *
"""
    Desde el lado del cliente...

"""

nombreServer = 'localhost'
puertoServer = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
"""
    AF_INET maneja un par de variables de tipo ("host":Str, "puerto":int) donde el host puede ser una dirección de ip
    o bien, una dirección de internet ej: google.com.ar
"""
clientSocket.connect((nombreServer,puertoServer))

oracion = input("Ingrese oracion: \n")

clientSocket.send(oracion.encode())

oracionMayuscula = clientSocket.recv(1024)

print("Oracion recibida y cambiada a mayuscula: \n" + oracionMayuscula.decode())

clientSocket.close()