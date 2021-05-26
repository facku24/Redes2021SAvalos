""" 
    Dado que estamos buscando crear una conexión cliente - servidor tipo TCP. Lo primero que deberíamos establecer
    es el protocolo de enlace y, además, establecer la conexion TCP.
    Un extremo tiene el socket del cliente (TCP) y, el otro, tiene el socket del servidor (TCP).
    DEBE ESTAR ESTABLECIDA LA CONEXION TCP! El cliente tiene el trabajo de iniciar contacto con el servidor. A su vez,
    el servidor ya tiene que estar listo (orden: 1) levanto server - 2) activo el cliente)
    El servidor también tiene que tener una respuesta espcial para el cliente.

    El cliente debe crear un SOCKET TCP especificando a QUE SOCKET del SERVIDOR (IP y Puerto) va a "hablar".
    El proceso del cliente llama a la puerta de bienvenida del proceso del servidor

    Cliente ---> ClientSocket
    Servidor --> ConnectionSocket
"""
from socket import *

nombreDelServer = 'localhost'
puertoDelServer = 12000

socketDelServidor = socket(AF_INET,SOCK_STREAM)
"""
    AF_INET familia de direcciones con forma (Dirección, Puerto)
    SOCK_STREAM establece conecxión tipo TCP
"""
socketDelServidor.bind((nombreDelServer,puertoDelServer))
#.bind() <-- el parámetro es una tupla. Por tal motivo va ()
# como también es un método de socket, lleva () --> queda: .bind((tupla))

socketDelServidor.listen(1)

print("SERVIDOR ESCUCHANDO EN PUERTO " + str(puertoDelServer) + " :")

while 1:
    connectionSocket, addr = socketDelServidor.accept()
    sentence = connectionSocket.recv(1024)
    oracionMayuscula = sentence.upper()
    connectionSocket.send(oracionMayuscula)
    connectionSocket.close()
