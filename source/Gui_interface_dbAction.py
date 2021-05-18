# Create: creare nuovi dipendenti e nuove zone associate ai dipendenti tramite l’ID
# Read: leggere dati relativi a zone e/o dipendenti
# Update: modificare le anagrafiche dei dipendenti o delle zone
# Delete: cancellare dati relativi a dipendenti e/o zone.


# i decide to split some Gui code to make it easy to understand
from tkinter import *
from tkinter import messagebox
from source import Client as cl


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def correct_authentication(window):

    new_window = Tk()
    new_window.title("Work page")
    new_window.geometry("520x420")
    new_window.config(background="#801d2b")

    frame_work = Frame(new_window,
                       bg="#801d2b",
                       )
    frame_work.pack(pady=75)

    label_title = Label(frame_work,
                        text="Ufficio risorse umane", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b", )
    label_title.grid(row=0, columnspan=3, pady=6, padx=3)

    pul_1 = Button(frame_work, text="Create", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=create,
                   )
    pul_1.grid(row=1, column=0, pady=6, padx=3)

    pul_2 = Button(frame_work, text="Read", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=read_db,
                   )
    pul_2.grid(row=2, column=0, pady=6, padx=3)

    pul_3 = Button(frame_work, text="Update", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=update,
                   )
    pul_3.grid(row=1, column=2, pady=6, padx=3)

    pul_4 = Button(frame_work, text="Delete", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=delete,
                   )
    pul_4.grid(row=2, column=2, pady=6, padx=3)

    # ------------New Window----------
    window.destroy()  # delete the old window


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def create():  # add someone to the db
    # ------------------gender-----
    def get_gender():
        if val.get() == 0:
            print("maschio")
        else:
            print("femmina")

    # ------------------------------
    text = "Add Page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("620x520")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=75)

    label_title = Label(frame_work, text="Add client", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=5, pady=6, padx=3)

    # ------------------------NAME---------------------------
    label_name = Label(frame_work, text="Nome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_name.grid(row=1, column=0, pady=6, padx=3, sticky=W)

    entry_name = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_name.grid(row=1, column=1)
    # -----------------------------------------------------------
    # --------------------SURENAME---------------------------
    label_surename = Label(frame_work, text="Cognome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_surename.grid(row=2, column=0, pady=6, padx=3, sticky=W)

    entry_surename = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_surename.grid(row=2, column=1)
    # -----------------------------------------------------------
    # --------------------OCCUPATION-----------------------------
    label_occupation = Label(frame_work, text="Occupazione:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=3, column=0, pady=6, padx=3, sticky=W)

    entry_occupation = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_occupation.grid(row=3, column=1)
    # -----------------------------------------------------------
    # ---------------------WORK ZONE-----------------------------
    label_zone = Label(frame_work, text="Zona di lavoro:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_zone.grid(row=4, column=0, pady=6, padx=3, sticky=W)

    entry_zone = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_zone.grid(row=4, column=1)
    # -----------------------------------------------------------
    # -------------------------DATE------------------------------
    label_date = Label(frame_work, text="emploimynt date:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_date.grid(row=1, column=2, pady=6, padx=3, sticky=W)

    entry_nome = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_nome.grid(row=1, column=3)
    # -----------------------------------------------------------
    # ----------------------EARNING------------------------------
    label_eanrning = Label(frame_work, text="Stipendio:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_eanrning.grid(row=2, column=2, pady=6, padx=3, sticky=W)

    entry_eanrning = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_eanrning.grid(row=2, column=3)
    # -----------------------------------------------------------
    # ---------------------------GENDER--------------------------
    label_gender = Label(frame_work, text="Sesso:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_gender.grid(row=3, column=2, pady=6, padx=3, sticky=W)

    G = ["M", "F"]
    val = IntVar()
    for i in range(len(G)):
        radio_gender = Radiobutton(frame_work, text=G[i], value=i, variable=val, bg="#801d2b", activeforeground="white",
                                   activebackground="#801d2b", command=get_gender)
        if i == 0:
            radio_gender.grid(row=3, column=3, sticky=W)
        else:
            radio_gender.grid(row=3, column=3, sticky=E)
    # -----------------------------------------------------------
    # --------------------CLIENT NUMEBR--------------------------
    label_number = Label(frame_work, text="Numero Clienti:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_number.grid(row=4, column=2, pady=6, padx=3, sticky=W)

    entry_number = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_number.grid(row=4, column=3)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Add", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, )
    send.grid(row=5, columnspan=5, pady=6, padx=3)

    # Devi farmi un dizionario con tutti i valori interni

    cl.insert(dizionario)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def read_db():  # raad someones data from DB
    def find():
        data = "this will show the resuslt of a query"
        db_data = Label(frame_work, text=data, font=("Arial", 14, "normal"), fg="#edb415")
        db_data.grid(row=3, columnspan=5, pady=10)

    text = "Read page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("620x520")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=75)

    label_title = Label(frame_work, text="Read from DB", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=5, pady=6, padx=3)

    # ------------------------NAME---------------------------
    label_name = Label(frame_work, text="Nome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_name.grid(row=1, column=0, pady=6, padx=3, sticky=W)

    entry_name = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_name.grid(row=1, column=1)
    # -----------------------------------------------------------
    # --------------------SURENAME---------------------------
    label_surename = Label(frame_work, text="Cognome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_surename.grid(row=1, column=2, pady=6, padx=3, sticky=W)

    entry_surename = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_surename.grid(row=1, column=3)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Search", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, command=find)
    send.grid(row=2, columnspan=5, pady=6, padx=3)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def seValueForm(frame_work):
    # ------------------gender-----
    def get_gender():
        if val.get() == 0:
            print("maschio")
        else:
            print("femmina")

    # ------------------------------

    # ------------------------NAME---------------------------
    label_name = Label(frame_work, text="Nome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_name.grid(row=3, column=0, pady=6, padx=3, sticky=W)

    entry_name = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_name.grid(row=3, column=1)
    # -----------------------------------------------------------
    # --------------------SURENAME---------------------------
    label_surename = Label(frame_work, text="Cognome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_surename.grid(row=4, column=0, pady=6, padx=3, sticky=W)

    entry_surename = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_surename.grid(row=4, column=1)
    # -----------------------------------------------------------
    # --------------------OCCUPATION-----------------------------
    label_occupation = Label(frame_work, text="Occupazione:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=5, column=0, pady=6, padx=3, sticky=W)

    entry_occupation = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_occupation.grid(row=5, column=1)
    # -----------------------------------------------------------
    # ---------------------WORK ZONE-----------------------------
    label_zone = Label(frame_work, text="Zona di lavoro:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_zone.grid(row=6, column=0, pady=6, padx=3, sticky=W)

    entry_zone = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_zone.grid(row=6, column=1)
    # -----------------------------------------------------------
    # -------------------------DATE------------------------------
    label_date = Label(frame_work, text="emploimynt date:", font=("Arial", 14, "normal"), fg="#edb415",
                       bg="#801d2b", )
    label_date.grid(row=3, column=2, pady=6, padx=3, sticky=W)

    entry_nome = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_nome.grid(row=3, column=3)
    # -----------------------------------------------------------
    # ----------------------EARNING------------------------------
    label_eanrning = Label(frame_work, text="Stipendio:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_eanrning.grid(row=4, column=2, pady=6, padx=3, sticky=W)

    entry_eanrning = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_eanrning.grid(row=4, column=3)
    # -----------------------------------------------------------
    # ---------------------------GENDER--------------------------
    label_gender = Label(frame_work, text="Sesso:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_gender.grid(row=5, column=2, pady=6, padx=3, sticky=W)

    G = ["M", "F"]
    val = IntVar()
    for i in range(len(G)):
        radio_gender = Radiobutton(frame_work, text=G[i], value=i, variable=val, bg="#801d2b",
                                   activeforeground="white",
                                   activebackground="#801d2b", command=get_gender)
        if i == 0:
            radio_gender.grid(row=5, column=3, sticky=W)
        else:
            radio_gender.grid(row=5, column=3, sticky=E)
    # -----------------------------------------------------------
    # --------------------CLIENT NUMEBR--------------------------
    label_number = Label(frame_work, text="Numero Clienti:", font=("Arial", 14, "normal"), fg="#edb415",
                         bg="#801d2b", )
    label_number.grid(row=6, column=2, pady=6, padx=3, sticky=W)

    entry_number = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_number.grid(row=6, column=3)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Update", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, )
    send.grid(row=7, columnspan=5, pady=6, padx=3)


# --------------------------------------------------------------------------------------------------------


def update():  # update someones data

    text = "update page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("620x520")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=75)

    label_title = Label(frame_work, text="Update DB", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=5, pady=6, padx=3)

    # ------------------------NAME---------------------------
    label_name = Label(frame_work, text="Nome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_name.grid(row=1, column=0, pady=6, padx=3, sticky=W)

    entry_name = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_name.grid(row=1, column=1)
    # -----------------------------------------------------------
    # --------------------SURENAME---------------------------
    label_surename = Label(frame_work, text="Cognome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_surename.grid(row=1, column=2, pady=6, padx=3, sticky=W)

    entry_surename = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_surename.grid(row=1, column=3)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Search", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, command=update)
    send.grid(row=2, columnspan=5, pady=6, padx=3)

    # request from db
    data = cl.getExistDipendente()

    # set value on UI
    seValueForm()


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def delete():  # delete someone information from db
    def eliminate():
        if messagebox.askokcancel(title="Are you sure", message="delete user?", ):
            print("query to delete usere")
            mess = Label(frame_work, text="user deleted", font=("Arial", 14, "normal"), fg="#edb415")
            mess.grid(row=3, columnspan=5, pady=10)
        else:
            print("option canceld")

    text = "Delete page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("620x520")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=75)

    label_title = Label(frame_work, text="Delete from DB", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=5, pady=6, padx=3)

    # ------------------------NAME---------------------------
    label_name = Label(frame_work, text="Nome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_name.grid(row=1, column=0, pady=6, padx=3, sticky=W)

    entry_name = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_name.grid(row=1, column=1)
    # -----------------------------------------------------------
    # --------------------SURENAME---------------------------
    label_surename = Label(frame_work, text="Cognome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_surename.grid(row=1, column=2, pady=6, padx=3, sticky=W)

    entry_surename = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_surename.grid(row=1, column=3)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Delete", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10,
                  command=eliminate)
    send.grid(row=2, columnspan=5, pady=6, padx=3)
