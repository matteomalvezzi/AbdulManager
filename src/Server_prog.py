# ___________________________________________________Import some libraries
import socket
import concurrent.futures

# ___________________________________________________Create Socket
host = "localhost"
port = 15000

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sok.bind((host, port))
user_number = 5
sok.listen(user_number)
# ___________________________________________________Start

print("//___Server avviato___//")


# ___________________________________________________Method that manage all

def connect_db(conn, addr):
    conn.send("//___Benvenuto___//\nInserire la password:".encode())
    password = conn.recv(1024).decode()

    if password == "qwerty":
        conn.send("Connesso con successo".encode())
    else:
        conn.send("password errata".encode())


# _____________________________________________________Multi thread loop

while True:
    conn, addr = sok.accept()
    print("connesso a:", addr)
    concurrent.futures.ThreadPoolExecutor(max_workers=user_number).submit(connect_db, conn, addr)
