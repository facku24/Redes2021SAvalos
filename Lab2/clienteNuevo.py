import socket 
import constantes
import base64

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
        self.client.shutdown(socket.SHUT_RDWR)

#---------

client = Client(constantes.host,constantes.port)

while True: 
    message = input("Send some data here -> ")
    client.send_request(message)
    print("Got response from server:\n")
    response = client.recive_response()
    if message.split(' ')[0] == "get":
        try:
            with open (f"copy{message.split(' ')[1]}","wb") as recivedfile:
                recivedfile.write(base64.b64decode(response))
                response = "Success received file from server"
        
        except IOError as error:
            response = "Failed"

    print (response)
    if response == "CONEXION CLOSED":
        client.close_connection()
        break