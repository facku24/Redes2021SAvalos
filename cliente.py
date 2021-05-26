from socket import *

class Client(object):
    def __init__(self,host,port):
        """
            Constructor de la clase Cliente. Que tiene??
        """
        self.create_socket(host, port)
    
    def create_socket(self, host, port):
        """
            Creará un socket con las direcciones provistas (adress y port).
        """
        self.socket_client = socket (AF_INET,SOCK_STREAM)
        self.socket_client.connect((host,port))

    def send_data(self, message:str):
        """
            Enviara un mensaje codificado.-
        """
        self.socket_client.send(message.encode())
    
    def recibe_data(self):
        """
            Recibe un mensaje decodificado.-
            Para ello el server, tiene que enviar el mensaje
        """
        message_received = self.socket_client.recv(1024).decode()
        return message_received
    
    def close_connection(self):
        """
            Cierra el socket del lado del cliente
        """
        self.socket_client.close()



if __name__ == "__main__":

    host = gethostname() 
    port = 12000

    myClient = Client(host,port)
    
    message = input("Ingrese oración:\n")
    myClient.send_data(message)
    print(myClient.recibe_data())
    myClient.close_connection()
