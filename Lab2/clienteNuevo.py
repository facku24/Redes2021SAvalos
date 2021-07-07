import socket 
import constantes

class Client(object):
    def __init__(self,host,port):
        self.create_socket(host, port)
    
    def create_socket(self, host, port):
        self.client = socket.socket()
        client = self.client.connect((host,port))
    
    def send_request (self, request:str):
        self.client.send(request.encode())
    
    def recive_response(self):
        response_recive = self.client.recv(1024).decode()
        return response_recive
    
    def close_connection(self):
        self.client.close()

#---------

client = Client(constantes.host,constantes.port)

while True: 
    message = input("Send some data here -> ")
    client.send_request(message)
    print("Got response from server:\n")
    print(client.recive_response())
    
"""

client.sendall(send_message.encode()) #hasta aqui envio de mensaje
#-----
response = client.recv(1024).decode()
print (int(response))
client.close
"""