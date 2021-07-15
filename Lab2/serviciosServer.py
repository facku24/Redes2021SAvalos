from os import getcwd, scandir, listdir
import base64

def list_files ():
    """
    Lista de archivos del servidor.
    """
    response = listdir(getcwd())
    return "Listing available files from the server...: \n"+"="*80+"\n"+'\n'.join(response)+"\n"+"="*80

def get_files (filetxt):
    try:
        with open (filetxt,"rb") as filetosend:
            size = 2048
            response = bytes()
            buffer = filetosend.read(size)
            while buffer:
                response += buffer
                buffer = filetosend.read(size)

            return base64.b64encode(response).decode()
	
    except IOError as error:
        response = "File not found"
	
    finally:
        filetosend.close()

    return response

def metadata_files(filetxt):
    fileDir = list(scandir())
    fileObject = None
    for i in fileDir:
        if i.name == filetxt: 
            fileObject = i 
            break
    
    metadata = tuple(fileObject.stat())
    return f"""{fileObject.name} METADATA INFORMATION: 
    ------------------------------------
    Mode: {metadata[0]},
    Device Id: {metadata[2]},
    Owner: {metadata[4]},
    File Size: {metadata[6]} bytes,
    ------------------------------------"""

def close_conexion():
    return "CONEXION CLOSED"

list_functions = {
    "LIST": list_files,
    "GET": get_files,
    "METADATA": metadata_files,
    "CLOSE": close_conexion
}

def serve(request: str):
    response = None
    request_splited = request.split(' ')
    if len(request_splited) == 1 and request_splited[0].upper() in list_functions:
        response = list_functions[request_splited[0].upper()]()
    elif len(request_splited) == 2 and request_splited[0].upper() in list_functions:
        response = list_functions[request_splited[0].upper()](request_splited[1])
    else:
        response = ' '.join(request_splited).upper() 
    
    return response