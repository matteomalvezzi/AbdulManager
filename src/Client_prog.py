# ___________________________________________________Import some libraries
import socket
from Python_project.src import Gui_interface

def getExistDipendente():
    dati = {}
    return dati

def insert( dati ):


    #1. check che tutti i dati siano integri
    #2. send verso il server dei dati

    pass

def update ( dati ):
    #1. controllo
    #2. inserisco
    pass




# ___________________________________________________Create Socket
host="localhost"
port=15000

sok=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sok.connect((host,port))
#--------------------After connection start gui
Gui_interface.gui(sok)
# ___________________________________________________Send and recv START

# while True:
#     dati_1=sok.recv(1024).decode()
#     print(dati_1)
#     sok.send(input().encode())
#     dati_2=sok.recv(1024).decode()
#     print(dati_2)
