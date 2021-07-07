import select
import socket
import serviciosServer
import constantes

class Server(object):
    def __init__ (self, host, port, listener_number):
        self.create_socket(host, port, listener_number)
    
    def create_socket(self, host, port, listener_number):
        self.welcome_socket = socket.socket()
        self.welcome_socket.bind((host,port))
        self.welcome_socket.listen(listener_number)
    
    def create_connection (self):
        self.connection_socket, self.adrss = self.welcome_socket.accept() #tupla
    
    def recive_request(self):
        return self.connection_socket.recv(1024).decode()
    
    def send_response (self, response):
        self.connection_socket.send(response.encode())
    
    def close_server_socket(self):
        self.connection_socket.close()

print("Waiting for client...")
server = Server(constantes.host, constantes.port, constantes.listener)
server.create_connection()

while True:
    recived_request = server.recive_request()
    response = serviciosServer.serve(recived_request)
    server.send_response(response)


"""
    #aqui recibo datos y tendría que ver que pasa si
    #data es un string o no o si es una función
    Si el string es una de las funciones, tengo que hacer lo que pide List -> list..
    #connection.sendall(added_data.encode())
    #sizefile = os.stat('archivo del que quiero saber el tamaño').st_size -> print(sizefile) 
"""