from socket import *

class Server(object):
    
    def __init__(self,ip_Server, port_Server):
        """
            Constructor/inicializador
        """
        self.create_socket(ip_Server,port_Server)

    def create_socket(self, ip_Server, port_Server):
        """
            Creará un socket con las direcciones provistas (adress y port).
            Return socket creado.
        """
        self.socket_server = socket (AF_INET,SOCK_STREAM)
        self.socket_server.bind((ip_Server, port_Server))
        self.socket_server.listen(1)
        print ("Servidor escuchando en puerto " +str(port_Server)+ " del server " + str(ip_Server))
        self.connectionSocket, self.adrss = self.socket_server.accept()

    def recive_data(self):
        """
            Recibe la información codificada (en minuscula)
            Return la información modificada (en mayuscula)
        """
        sentence = self.connectionSocket.recv(1024)
        capitalizedSentence = sentence.decode().upper()
        return capitalizedSentence

    
    def send_data(self,data):
        """
            Enviará información modificada (en mayusculas)
        """
        self.connectionSocket.send(data.encode())
    
    def close_socket(self):
        """
            Cerrará el socket abierto
        """
        self.connectionSocket.close()


if __name__ == '__main__':
    ip_Server = gethostname()
    port_Server = 12000

    myServer = Server(ip_Server,port_Server)

    while 1:
        data = myServer.recive_data()
        myServer.send_data(data)
        myServer.close_socket()