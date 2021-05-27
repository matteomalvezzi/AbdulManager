# ___________________________________________________Import some libraries
import socket as sock
import sys
from AbdulManager.AbdulManager.source import Gui_interface


#___________________________________________________ Do command  ___________________________________________________

def get_all_dipendenti(sock_client):
    sock_client.send("get_all_dipendenti".encode())
    response =sock_client.recv(4096).decode()
    return response

def getSedi( sock_client ):     #Get list of sedi from server
    sock_client.send("get_all_sedi".encode())
    response = sock_client.recv(4096).decode()
    lista_sedi = eval(response)
    return lista_sedi

def get_id_sede(sock_client,info_sede):
    sock_client.send("get_id_sede".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(str(info_sede).encode())

        id_sede = sock_client.recv(4096).decode()
        return id_sede

def getReparti( sock_client, sede ): #Get list of reparti from server with information about sede
    sock_client.send("get_all_reparti".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(sede.encode())

        response = sock_client.recv(4096).decode()
        lista_reparti = eval(response)
        print("Ecco i reparti di questa sede: " + str(lista_reparti))
        return lista_reparti

def getImpieghi( sock_client ): #Get list of impieghi from server
    sock_client.send("get_all_impieghi".encode())
    response = sock_client.recv(4096).decode()
    lista_sedi = eval(response)
    return lista_sedi

def insertDipendente( sock_client, new_dipendente ):    #Insert dipendente and send to server dipendente's informations
    sock_client.send("insert_dipendente".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(str(new_dipendente).encode())

        response = sock_client.recv(4096).decode()
        print(response)

def insertSede( sock_client, sede ):  #Insert sede
    sock_client.send("insert_sede".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(str(sede).encode())

        response = sock_client.recv(4096).decode()
        print(response)

def insertReparto( sock_client, reparto): #Insert reparto
    sock_client.send("insert_reparto".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(str(reparto).encode())

        response = sock_client.recv(4096).decode()
        print(response)

def insertImpiego( sock_client, impiego):   #Insert impiego
    sock_client.send("insert_impiego".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(impiego.encode())

        response = sock_client.recv(4096).decode()
        print(response)

def getDipendenteNome ( sock_client, nome, cognome)  :
    sock_client.send("get_dipendente_nome".encode())
    response = sock_client.recv(4096).decode()

    if response == "pronto":
        info_dip = str(nome) + " " + str(cognome)
        print("'info dip'"+info_dip)
        sock_client.send(info_dip.encode())

        response = sock_client.recv(4096).decode()
        print(response)
        info_dipendente = eval(response)
        return info_dipendente

def getDipendenteCf(sock_client, cf):
    sock_client.send("get_dipendente_cf".encode())
    response = sock_client.recv(4096).decode()

    if response == "pronto":
        sock_client.send(cf.encode())
        response = sock_client.recv(4096).decode()

        info_dipendente = eval(response)
        return info_dipendente

def getInfoReparto(sock_client, id_reparto):
    sock_client.send("get_reparto_name".encode())
    response = sock_client.recv(4096).decode()

    if response == "pronto":
        sock_client.send(str(id_reparto).encode())
        response = sock_client.recv(4096).decode()

        info_reparto = eval(response)
        print(info_reparto)
        return info_reparto

def getInfoSede(sock_client, id_sede):
    sock_client.send("get_sede_name".encode())
    response = sock_client.recv(4096).decode()

    if response == "pronto":
        sock_client.send(str(id_sede).encode())
        response = sock_client.recv(4096).decode()

        info_sede = eval(response)
        print(info_sede)
        return info_sede


def getInfoImpiego(sock_client, id_impiego):
    sock_client.send("get_name_impiego".encode())
    response = sock_client.recv(4096).decode()

    if response == "pronto":
        sock_client.send(str(id_impiego).encode())
        response = sock_client.recv(4096).decode()

        info_impiego = eval(response)
        print(info_impiego)
        return info_impiego

def updateDipendente( sock_client, exist_dipendente_data ):    #Update dipendente and send to server dipendente's informations
    sock_client.send("update_dipendente".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(str(exist_dipendente_data).encode())

        response = sock_client.recv(4096).decode()
        print(response)

def deleteDipendente( sock_client, id_dipendente ):
    sock_client.send("delete_dipendente".encode())
    response = sock_client.recv(4096).decode()
    if response == "pronto":
        sock_client.send(str(id_dipendente).encode())

        response = sock_client.recv(4096).decode()
        print(response)

#___________________________________________________ Send for command to socket server  ___________________________________________________
def send_command_to_server(client_sock, command):

    #client_sock.send(comando)
    pass

#___________________________________________________ Send for authentication to socket server  ___________________________________________________
def send_password_to_server( username , password, client_sock ):

    client_sock.send(username.encode())
    response = client_sock.recv(4096)

    #get response about username from server
    if response.decode() == "user_not_exist":
        Gui_interface.show_message_box("Utente inesistente")
        return False

    elif response.decode() == "user_correct":
        #send password
        client_sock.send(password.encode())
        response = client_sock.recv(4096).decode()

        #get response about password from server
        if response == "password_not_correct":

            Gui_interface.show_message_box("Password errata")
            return False

        elif response == "password_correct":

            print("Username e password corretti accesso eseguito correttamente")
            return True

    else:

        print("Tenativi falliti, Accesso respinto")

        client_sock.close()

        Gui_interface.show_message_box("Tentativi esauriti")

        sys.exit()

#___________________________________________________ Create socket client  ___________________________________________________
def create_socket_client(indirizzo_server):

    try:
        client_sock = sock.socket()
        client_sock.connect(indirizzo_server)
        print("Connessione al server: "+str(indirizzo_server))

        print(client_sock)
        Gui_interface.gui(client_sock)  # Start Gui interface

    except sock.error as errore:
        print(errore)
        print("Problema di connessione al server..")
        sys.exit()


#___________________________________________________ Main ___________________________________________________
if __name__ == '__main__':

    server = ("localhost", 15000)   #socket server information

    #server = ("ec2-18-133-221-171.eu-west-2.compute.amazonaws.com", 15000)  # socket server information

    create_socket_client(server)  # Create socket client that will connect to socket server

