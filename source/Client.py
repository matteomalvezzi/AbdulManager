# ___________________________________________________Import some libraries
import socket as sock
import sys
from source import Gui_interface

global client_sock


#___________________________________________________ Do command  ___________________________________________________
def insertDipendente( new_dipendente ):
    #1. check che tutti i dati siano integri
    #2. send verso il server dei dati
    pass

def update ( dati ):
    #1. controllo
    #2. inserisco
    pass



#___________________________________________________ Send for command to socket server  ___________________________________________________
def send_command_to_server(client_sock, command):

    #client_sock.send(comando)
    pass

#___________________________________________________ Send for authentication to socket server  ___________________________________________________
def send_password_to_server( username , password ):

    while True:
        #send username
        client_sock.send(username.encode())
        response = client_sock.recv(4096)

        #get response about username from server
        if response.decode() == "user_not_exist":
            Gui_interface.show_message_box("Password errata")
            continue

        elif response.decode() == "user_correct":
            #send password
            client_sock.send(password.encode())
            response = client_sock.recv(4096).decode()

            #get response about password from server
            if response == "password_not_correct":

                Gui_interface.show_message_box("Password errata")
                continue

            elif response == "password_correct":

                print("Username e password corretti accesso eseguito correttamente")
                return True

        else:

            print("Tenativi falliti, Accesso respinto")

            client_sock.close()

            return False

#___________________________________________________ Create socket client  ___________________________________________________
def create_socket_client(indirizzo_server):

    try:
        client_sock = sock.socket()
        client_sock.connect(indirizzo_server)
        print("Connessione al server: "+str(indirizzo_server))

    except sock.error as errore:
        print("Problema di connessioen al server..")
        sys.exit()


#___________________________________________________ Main ___________________________________________________
if __name__ == '__main__':

    server = ("localhost", 15000)   #socket server information

    Gui_interface.gui()          #Start Gui interface

    create_socket_client(server)    #Create socket client that will connect to socket server
