# ___________________________________________________Import some libraries
import pickle
import socket as sock
import threading
import mariadb


def sql_safe(field):
    return str(field.replace("'", "''"))
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

    cursor = db_connection.cursor()
    query= "SELECT username FROM login_user WHERE username='" + sql_safe(username) + "'"
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
    query= "SELECT password FROM login_user WHERE username= '" + sql_safe(username) + "'"
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

# ___________________________________________________Execute Command ___________________________________________________

# ___________________________________________________GET IMPIEGHI, SEDI, REPARTI ___________________________________________________
def get_all_impieghi ():
    cursor = db_connection.cursor()
    query= "SELECT * FROM abdulmanager.impieghi;"
    cursor.execute(query)
    result_set = cursor.fetchall()
    list_impieghi = []
    for row in result_set:
        list_impieghi.append(row[1])
    return list_impieghi

def get_all_sedi ():
    cursor = db_connection.cursor()
    query= "SELECT * FROM abdulmanager.sedi;"
    cursor.execute(query)
    result_set = cursor.fetchall()
    lista_sedi = []
    for row in result_set:
        sede= []
        sede.append(row[1])
        sede.append(row[2])
        sede.append(row[3])
        lista_sedi.append(sede)
    return lista_sedi

def get_all_reparti ( id ):
    cursor = db_connection.cursor()
    query= "SELECT * FROM abdulmanager.reparti WHERE id_sede = '" + str(id) +"';"
    cursor.execute(query)
    result_set = cursor.fetchall()
    lista_reparti = []
    for row in result_set:
        lista_reparti.append(row[1])
    return lista_reparti

def get_id_sede ( indirizzo, citta, provincia ):
    cursor = db_connection.cursor()
    query = "SELECT id FROM abdulmanager.sedi WHERE indirizzo = '" + sql_safe(indirizzo) + "' AND citta = '" + sql_safe(citta) + "' AND provincia = '" + sql_safe(provincia) + "';"
    cursor.execute(query)
    result_set = cursor.fetchall()
    row = result_set[0]
    return row[0]

# ___________________________________________________GET ID IMPIEGO ___________________________________________________
def get_id_impiego ( nome_impiego ):
    cursor = db_connection.cursor()
    query = "SELECT id FROM abdulmanager.impieghi WHERE impiego = '" + sql_safe(nome_impiego) + "';"
    cursor.execute(query)
    result_set = cursor.fetchall()
    row = result_set[0]
    return row[0]


# ___________________________________________________INSERT SEDE, REPARTO, IMPIEGO___________________________________________________
def insert_sede ( info_sede ):
    cursor = db_connection.cursor()
    info_sede = eval(info_sede)
    query= "INSERT INTO abdulmanager.sedi VALUES (null, '" + sql_safe(info_sede["indirizzo"]) + "', '" + sql_safe(info_sede["citta"]) + "', '" + sql_safe(info_sede["provincia"]) + "', '" + sql_safe(info_sede["cap"])+ "')"
    print(query)
    try:
        #cursor.execute("INSERT INTO abdulmanager.sedi(indirizzo, citta, provincia, cap) VALUES (? , ? , ? , ?)", (sql_safe(info_sede["indirizzo"]), sql_safe(info_sede["citta"]), sql_safe(info_sede["provincia"]), sql_safe(info_sede["cap"])))
        #cursor.execute("INSERT INTO abdulmanager.sedi(indirizzo, citta, provincia, cap) VALUES (? , ? , ? , ?)", (info_sede["indirizzo"], info_sede["citta"], info_sede["provincia"], info_sede["cap"]))
        cursor.execute(query)
        print("inserimento sede andato a buon fine")
    except Exception as e:
        print(e)
        print("errore nell'inserimento di una sede")



def insert_reparto ( info_reparto ):
    cursor = db_connection.cursor()
    query = "INSERT INTO abdulmanager.reparti VALUES (null, '" + sql_safe(info_reparto["nome_reparto"]) + "', '" + sql_safe(info_reparto["id_sede"]) + "')"
    cursor.execute(query)

def insert_impiego ( impiego ):
    cursor = db_connection.cursor()
    query = "INSERT INTO abdulmanager.impieghi VALUES (null, '" + sql_safe(impiego) +"');"
    cursor.execute(query)

# ___________________________________________________GET DIPENDENTE ___________________________________________________
def get_dipendente ( nome, cognome):
    cursor = db_connection.cursor()
    query = "SELECT * FROM abdulmanager.dipendente d INNER JOIN reparto_dipendenti rd ON d.id = rd.id_dipendente WHERE d.nome = '" + sql_safe(nome) + "' AND d.cognome = '" + sql_safe(cognome) + "';"
    cursor.execute(query)
    result_set = cursor.fetchall()
    dipendente_data= list(result_set[0])
    dipendente_data[4] = dipendente_data[4].strftime("%Y-%m-%d")
    dipendente_data[8] = dipendente_data[8].strftime("%Y-%m-%d")
    return dipendente_data

def get_dipendente_cf ( codice_fiscale ):
    cursor = db_connection.cursor()
    query = "SELECT * FROM abdulmanager.dipendente d INNER JOIN reparto_dipendenti rd ON d.id = rd.id_dipendente WHERE d.codice_fiscale = '" + sql_safe(codice_fiscale) + "';"
    cursor.execute(query)
    result_set = cursor.fetchall()
    dipendente_data= list(result_set[0])
    dipendente_data[4] = dipendente_data[4].strftime("%Y-%m-%d")
    dipendente_data[8] = dipendente_data[8].strftime("%Y-%m-%d")
    return dipendente_data

# ___________________________________________________INSERT DIPENDENTE ___________________________________________________
def insert_dipendente ( dipendente_info, impiego_id, reparto_id ):
    cursor = db_connection.cursor()
    print(sql_safe(dipendente_info["nome"]))
    try:
        query = "INSERT INTO abdulmanager.dipendente VALUES (null, '" + sql_safe(dipendente_info["nome"]) + "', '" + sql_safe(dipendente_info["cognome"]) + "', '" + sql_safe(dipendente_info["sesso"]) + "', '" + sql_safe(dipendente_info["data_nascita"]) + "', '" + sql_safe(dipendente_info["luogo"]) + "', '" + sql_safe(dipendente_info["cf"]) + "', '" + str(impiego_id) + "', '" + sql_safe(dipendente_info["data_assunzione"]) + "', '" + sql_safe(dipendente_info["stipendio"]) + "');"
        print("Query eseguita: " + str(query))
        cursor.execute(query)
        get_id_query = "SELECT id FROM abdulmanager.dipendente WHERE codice_fiscale= '" + sql_safe(dipendente_info["cf"]) + "';"
        cursor.execute(get_id_query)
        result_set = cursor.fetchall()
        print("ID DEL NUOVO DIPENDENTE: " + str(result_set[0][0]))
        cross_query = "INSERT INTO abdulmanager.reparto_dipendenti VALUES ('" + result_set[0][0] + "', '" + reparto_id + "');"
        cursor.execute(cross_query)
    except Exception as e:
        print(e)

# ___________________________________________________GET NAME OF REPARTO ___________________________________________________
def get_single_reparto( id ):
    cursor = db_connection.cursor()
    try:
        search_query = "SELECT nome_reparto, id_sede FROM abdulmanager.reparti WHERE id = '" + id + "';"
        cursor.execute(search_query)
        result_set = cursor.fetchall()
        print( str(result_set[0][0]) + str(result_set[0][1]))
        return result_set[0]
    except Exception as e:
        print(e)

# ___________________________________________________GET INFO OF SEDE ___________________________________________________
def get_single_sede( id ):
    cursor = db_connection.cursor()
    try:
        search_query = "SELECT * FROM abdulmanager.sedi WHERE id = '" + id + "';"
        cursor.execute(search_query)
        result_set = cursor.fetchall()
        print(result_set[0])
        return result_set[0]
    except Exception as e:
        print(e)

# ___________________________________________________GET IMPIEGO ___________________________________________________
def get_impiego( id ):
    cursor = db_connection.cursor()
    try:
        search_query = "SELECT impiego FROM abdulmanager.impieghi WHERE id = '" + id + "';"
        cursor.execute(search_query)
        result_set = cursor.fetchall()
        print(result_set[0])
        return result_set[0]
    except Exception as e:
        print(e)

# ___________________________________________________UPDATE ___________________________________________________
def updateDipendente ( dipendente_info, impiego_id, dipendente_id, reparto_id):
    cursor = db_connection.cursor()
    print(sql_safe(dipendente_info["nome"]))
    try:
        query = "UPDATE abdulmanager.dipendente SET  nome = '" + sql_safe(dipendente_info["nome"]) + "', cognome = '" + sql_safe(dipendente_info["cognome"]) + "', sesso = '" + sql_safe(dipendente_info["sesso"]) + "', data_di_nascita = '" + sql_safe(dipendente_info["sesso"]) + "', luogo_di_nascita = '" + sql_safe(dipendente_info["luogo"]) + "', codice_fiscale = '" + sql_safe(dipendente_info["cf"]) + "', impiego = '" + str(impiego_id) + "', data_assunzione = '" + sql_safe(dipendente_info["data_assunzione"]) + "', stipendio = '" + sql_safe(dipendente_info["stipendio"]) + "' WHERE id = '" + dipendente_id + "';"
        print("Query eseguita: " + str(query))
        cursor.execute(query)
        get_id_query = "SELECT id FROM abdulmanager.dipendente WHERE codice_fiscale= '" + sql_safe(dipendente_info["cf"]) + "';"
        cursor.execute(get_id_query)
        result_set = cursor.fetchall()
        cross_query = "UPDATE abdulmanager.reparto_dipendenti SET id_reparto = '" + reparto_id + "' WHERE id_dipendente = '" + result_set[0][0] + "';"
        cursor.execute(cross_query)
    except Exception as e:
        print(e)

# ___________________________________________________ DELETE DIPENDENTE ___________________________________________________
def deleteDipendente ( dipendente_id ):
    cursor = db_connection.cursor()
    try:
        query = "DELETE FROM abdulmanager.dipendente WHERE id = '" + dipendente_id +"';"
        print("Query eseguita: " + str(query))
        cursor.execute(query)
        cross_query = "DELETE FROM abdulmanager.reparto_dipendenti WHERE id_dipendente = '" + dipendente_id + "';"
        cursor.execute(cross_query)
    except Exception as e:
        print(e)
# ___________________________________________________Get Command ___________________________________________________

def get_command (socket_server, client_address, conn_counter):

    while True:
        print("Aspetto ordini dal client numero : " + str(conn_counter))

        command = socket_server.recv(4096).decode()

        if command == "get_all_sedi":
            #------------------------------RICHIESTA LISTA SEDI------------------------------
            print("Richiesta lista sedi")
            lista_sedi = str(get_all_sedi())
            socket_server.send(lista_sedi.encode())

        elif command == "get_all_impieghi":
            # ------------------------------RICHIESTA LISTA IMPIEGHI------------------------------
            print("Richiesta lista impieghi")
            lista_impieghi = str(get_all_impieghi())
            socket_server.send(lista_impieghi.encode())

        elif command == "get_all_reparti":
            # ------------------------------RICHIESTA LISTA REPARTI DI UNA SEDE------------------------------
            print("Richiesta lista reparti con sede")
            socket_server.send("pronto".encode())
            sede = socket_server.recv(4096).decode()

            sede_list = sede.split(',')
            id_sede = get_id_sede( sede_list[0], sede_list[1], sede_list[2] )
            lista_reparti = str(get_all_reparti( id_sede ))
            socket_server.send(lista_reparti.encode())

        elif command == "insert_sede":
            # ------------------------------INSERIMENTO SEDE------------------------------
            print("Richiesta di insermento di una nuova sede")
            socket_server.send("pronto".encode())
            sede_data = socket_server.recv(4096).decode()

            try:
                insert_sede(sede_data)
                socket_server.send("inserimento completato".encode())
            except Exception as e:
                socket_server.send("inserimneto bloccato".encode())

        elif command == "insert_reparto":
            # ------------------------------INSERIMENTO REPARTO------------------------------
            print("Richiesta di insermento di una nuovo reparto")
            socket_server.send("pronto".encode())
            reparto_data = socket_server.recv(4096).decode()

            try:
                insert_sede(reparto_data)
                socket_server.send("inserimento completato".encode())
            except Exception as e:
                socket_server.send("inserimneto bloccato".encode())

        elif command == "insert_impiego":
            # ------------------------------INSERIMENTO IMPIEGO------------------------------
            print("Richiesta di insermento di un nuovo impiego")
            socket_server.send("pronto".encode())
            impiego_data = socket_server.recv(4096).decode()

            try:
                insert_impiego( impiego_data )
                socket_server.send("inserimento completato".encode())
            except Exception as e:
                socket_server.send("inserimneto bloccato".encode())

        elif command == "insert_dipendente":
            # ------------------------------INSERIMENTO DIPENDENTE------------------------------
            print("Richiesta di insermento di un nuovo dipendente")
            socket_server.send("pronto".encode())
            dipendente_data = socket_server.recv(4096).decode()

            try:
                dipendente_data = eval(dipendente_data)
                insert_dipendente(dipendente_data, get_id_impiego(dipendente_data["impiego"]))
                socket_server.send("inserimento completato".encode())
            except Exception as e:
                print(e)
                socket_server.send("inserimneto bloccato".encode())

        elif command == "get_dipendente_nome":
            # ------------------------------GET DIPENDENTE WITH NAME AND SURNAME  ------------------------------
            print("Richiesta di insermento di un nuovo dipendente con nome e cognome")
            socket_server.send("pronto".encode())
            dipendente_info = socket_server.recv(4096).decode()
            dipendente_info_list = dipendente_info.split(" ")
            try:
                nome = dipendente_info_list[0]
                cognome = dipendente_info_list[1]
                dipendente_data = str(get_dipendente( nome, cognome ))

                print("Ecco cosa ho ricevuto dal metodo: " + str(dipendente_data))
                socket_server.send(dipendente_data.encode())
            except Exception as e:
                socket_server.send("Dati non disponibili".encode())

        elif command == "get_dipendente_cf":
            # ------------------------------GET DIPENDENTE WITH CF ------------------------------
            print("Richiesta di insermento di un nuovo dipendente con il codice fiscale")
            socket_server.send("pronto".encode())
            cf = socket_server.recv(4096).decode()

            try:
                dipendente_data = str(get_dipendente_cf(codice_fiscale=cf))
                socket_server.send(dipendente_data.encode())
            except Exception as e:
                socket_server.send("Dati non disponibili".encode())
            pass
        elif command == "get_reparto_name":
            # ------------------------------GET NAME OF REPARTO ------------------------------
            print("Richiesta nome di un reparto")
            socket_server.send("pronto".encode())
            id_reparto = socket_server.recv(4096).decode()

            info_reparto = str(get_single_reparto( id_reparto ))
            socket_server.send(info_reparto.encode())
        elif command == "get_sede_name":
            # ------------------------------GET NAME OF SEDE WITH ID ------------------------------
            print("Richiesta di info su una sede")
            socket_server.send("pronto".encode())
            id_sede = socket_server.recv(4096).decode()

            info_sede = str(get_single_sede( id_sede ))
            socket_server.send(info_sede.encode())

        elif command == "get_name_impiego":
            # ------------------------------GET NAME OF IMPIEGO ------------------------------
            print("Richiesta di info su un impiego")
            socket_server.send("pronto".encode())
            id_impiego = socket_server.recv(4096).decode()

            info_impiego = str(get_impiego(id_impiego))
            socket_server.send(info_impiego.encode())
        elif command == "update_dipendente":
            # ------------------------------UPDATE DIPENDENTE ------------------------------
            print("Richiesta di aggiornamento dei dati di un dipendente")
            socket_server.send("pronto".encode())
            dipendente_data = socket_server.recv(4096).decode()

            try:
                dipendente_data = eval(dipendente_data)
                updateDipendente(dipendente_data, get_id_impiego(dipendente_data["impiego"], dipendente_data["id"]))
                socket_server.send("inserimento completato".encode())
            except Exception as e:
                print(e)
                socket_server.send("inserimneto bloccato".encode())

        elif command == "delete_dipendente":
            # ------------------------------REMOVE AND DELETE DIPENDENTE ------------------------------
            print("Richiesta di eliminazione di un dipendente")
            socket_server.send("pronto".encode())
            id_dipendente = socket_server.recv(4096).decode()

            try:
                deleteDipendente( id_dipendente )
                socket_server.send("eliminazione completato".encode())
            except Exception as e:
                print(e)
                socket_server.send("eliminazione bloccato".encode())


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
