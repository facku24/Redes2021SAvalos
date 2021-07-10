import select
import socket
import serviciosServer
import constantes
from datetime import datetime as dt

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
    
def record_log(connection_ip, connection_port, request_decoded):
    try:
        with open("serverlog.txt","a") as logfile:
            datetime = dt.now()
            log = f"[-->]On {datetime} got conecction from {connection_ip} on port {connection_port} with message {request_decoded}\n"
            logfile.write(log)
    
    except IOError as error:
        print ("couldn't opend logfile")


print("Waiting for client...")
server = socket.socket()
server.bind((constantes.host,constantes.port))
server.listen(constantes.listener)
inputs = [server]
outputs = []
errors = []
mesage = {}

while inputs:
    readable, writeable, exceptions = select.select(inputs,outputs,errors) 
    for r in readable:
        if r is server:
            connection_socket, adrss = r.accept() #acepta la conexion.
            inputs.append(connection_socket)
        
        else:
            recived_request = r.recv(1024)
            connection_ip , connection_port = r.getpeername()
            request_decoded = recived_request.decode()
            mesage[connection_port] = request_decoded
            if request_decoded != "":
                record_log(connection_ip, connection_port, request_decoded)

            if r not in outputs:
                outputs.append(r)

    for w in writeable:
        w_client_port = w.getpeername()[1] #conseguir el puerto del cliente (w)
        mesage_exist = mesage[w_client_port] #Verificacion de mensaje si existe o no. Si existe lo trae
        response = serviciosServer.serve(mesage_exist)
        if response == "CONEXION CLOSED":
            w.send(response.encode())
            if w in inputs:
                inputs.remove(w)
            w.shutdown(socket.SHUT_RDWR)
            del mesage[w_client_port]
        
        else:
            w.send(response.encode())

        outputs.remove(w)
        
    for e in exceptions:
        pass
