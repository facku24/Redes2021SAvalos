from socket import *
from os import getcwd, scandir, listdir
from typing import MutableMapping

class Server(object):
    
    def __init__(self,ip_Server, port_Server):
        """
            Constructor/inicializador
        """
        self.create_socket(ip_Server,port_Server)

    def create_socket(self, ip_Server, port_Server):
        """
            Creará un socket con las direcciones provistas (adress y port).
        """
        self.socket_server = socket(AF_INET,SOCK_STREAM)
        self.socket_server.bind((ip_Server, port_Server))
        self.socket_server.listen(1)
        print ("Servidor escuchando en puerto " +str(port_Server)+ " del server " + str(ip_Server))

    def recive_data(self):
        """
            Recibe la información codificada (en minuscula)
            Return la información modificada (en mayuscula)
        """
        self.connectionSocket, self.adrss = self.socket_server.accept()
        sentence = self.connectionSocket.recv(1024)
        capitalizedSentence = sentence.decode()#.upper()
        return capitalizedSentence

    
    def send_data(self,data:str):
        """
            Enviará información modificada (en mayusculas)
        """
        self.connectionSocket.send(data.encode())
    
    def close_socket(self):
        """
            Cerrará el socket abierto
        """
        self.connectionSocket.close()

#-----HASTA AQUI CLASE SERVER-----

def listar_archivo ():
    response = listdir(getcwd())
    return '\n'.join(response)

def obtener_archivo(file_name):
    try:
        fichero = open(f"{file_name}")
        lines = fichero.readlines()
        response = "".join(lines)
	
    except IOError as error:
        response = "File not found"
	
    finally:
        fichero.close()
        return response

def metadata_archivo(file_name):
    fDir = list(scandir()) #DirEntry object has various attributes and method which is used to expose the file path and other file attributes of the directory entry.
    fileObject = None
    for i in fDir:
        if i.name == file_name: 
            fileObject = i 
            break
    
    metadata = tuple(fileObject.stat()) #stat() method on os.DirEntry object is used to get os.stat_result object for an entry.
    return f"""{fileObject.name} METADATA INFORMATION: 
    
    Mode: {metadata[0]},
    Device Id: {metadata[2]},
    Owner: {metadata[4]},
    File Size: {metadata[6]} bytes,"""


def cerrar_conexion():
    return "CONEXION CLOSED"

#-----HASTA ACÁ LAS FUNCIONES DEL DICCIONARIO----- 
if __name__ == '__main__':
    ip_Server = gethostname()
    port_Server = 12013

    myServer = Server(ip_Server,port_Server)

    to_do_list = {
            "LIST": listar_archivo,
            "GET": obtener_archivo,
            "METADATA": metadata_archivo,
            "CLOSE": cerrar_conexion
    }
    
    while True:
        response = None
        data = myServer.recive_data().split(' ')

        if len(data) == 1 and data[0].upper() in to_do_list:
            response = to_do_list[data[0].upper()]()
        elif len(data) == 2 and data[0].upper() in to_do_list:
            try:
                response = to_do_list[data[0].upper()](data[1])
            except:
                response = "Error File not found..."
        else:
            response = ' '.join(data).upper()
        

        if data == "CONEXION CLOSED":
            myServer.send_data(response)
        
        else:
            myServer.send_data(response)
