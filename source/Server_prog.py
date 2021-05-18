# ___________________________________________________Import some libraries
import socket as sock
import threading
import mariadb



#___________________________________________________ Connection to mariadDB database ___________________________________________________
def connect_to_Database():
    # Connect to MariaDB Platform

    global db_connection
    try:
        db_connection = mariadb.connect(
            user="root",
            password="7637",
            host="localhost",
            port=3306,
            database="abdulmanager"
        )
    except mariadb.Error as e:
        db_connection = None
        connect_to_Database()
        print(f"Error connecting to MariaDB Platform: {e}")

#___________________________________________________ Get username ___________________________________________________
def get_user_from_DB(username):

    print("Tentativo di accesso, username: " + str(username))
    cursor = db_connection.cursor()
    query= "SELECT username FROM login_user WHERE username='" + str(username) + "'"
    cursor.execute(query)

    try:
        result_set = cursor.fetchall()
        for row in result_set:
            user = row[0]
            print(user)
            return user
    except Exception:
        print("ACCOUNT INESISTENTE")
        return None

#___________________________________________________ Get Password ___________________________________________________
def get_password_from_DB(username):

    cursor = db_connection.cursor()
    query= "SELECT password FROM login_user WHERE username= '" + str(username) + "'"
    cursor.execute(query)

    try:
        result_set = cursor.fetchall()
        for row in result_set:
            passwd = row[0]
            print(passwd)
            return passwd
    except Exception:
        print("ACCOUNT INESISTENTE")
        return None


# ___________________________________________________Start

def get_command (socket_server, client_address, conn_counter):

    print("Aspetto ordini dal client numero : " + str(conn_counter))

    command = socket_server.recv(4096)

    if command == 1:
        # insert dipendente
        pass
    elif command == 2:
        # elimina dipendente
        pass
    elif command == 3:
        # aggiorna dipendente
        pass
    elif command == 4:
        # visualizza dipendente
        pass



#___________________________________________________ Check password ___________________________________________________
def check_password(socket_server):

    connect_to_Database()

    accesso= False
    counter_tentativi = 0

    while not accesso:  #maximum attempts

        if counter_tentativi < 3:   #counter attempts

            #recive username
            recv =socket_server.recv(4096)
            print("Username " + recv.decode())

            #check if username exist
            username_db = get_user_from_DB( recv.decode() )

            if username_db is not None:

                socket_server.send("user_correct".encode())

                #recive password
                recv = socket_server.recv(4096)
                password = recv.decode()
                print("Password" + password)

                password_db = get_password_from_DB( username_db )

                #check if password from database is equals to inserted password
                if password == password_db:
                    socket_server.send("password_correct".encode())
                    return True
                else:
                    socket_server.send("password_not_correct".encode())
                    counter_tentativi = counter_tentativi + 1
            else:

                socket_server.send("user_not_exist".encode())
                counter_tentativi = counter_tentativi + 1

        else:
            accesso = True
            socket_server.send("Troppi tentativi".encode())

            return False


#___________________________________________________ Create start server socket and with thread accept new client ___________________________________________________
def start_server_socket(server_address, backlog=1):
    max_client_conn = 10

    try:
        socket_server = sock.socket()

        socket_server.bind(server_address)

        socket_server.listen(max_client_conn)

    except:

        print("Error")
        start_server_socket(server_address, backlog=1)

    thread = []
    conn_counter= 0

    while True:

        conn, client_address = socket_server.accept()

        isLogin = check_password(conn)

        if isLogin:

            conn_counter = conn_counter + 1

            t = threading.Thread(target=get_command, args=(conn, client_address, conn_counter, ))
            t.start()
            thread.append(t)

        else:

            conn.close()

    for thread_i in thread:
        thread_i.join()

#___________________________________________________ Main ___________________________________________________
if __name__ == '__main__':

    server_address = ("localhost", 15000) #tupla con indirizzo e porta
    start_server_socket(server_address)
