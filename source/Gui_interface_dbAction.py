# Create: creare nuovi dipendenti e nuove zone associate ai dipendenti tramite l’ID
# Read: leggere dati relativi a zone e/o dipendenti
# Update: modificare le anagrafiche dei dipendenti o delle zone
# Delete: cancellare dati relativi a dipendenti e/o zone.


# i decide to split some Gui code to make it easy to understand
from tkinter import *
from tkinter import messagebox
from source import Client as cl
from tkinter import ttk

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def correct_authentication(window, socket_client):

    global cl_sock
    cl_sock = socket_client

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
                   command= create,
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

    # Get dropdown data

    # print("Ciao")
    #
    # lista_sedi = cl.getSedi(cl_sock)
    #
    # sede1 = lista_sedi[0]
    # for sede in lista_sedi:
    #     #set value of dropdown section
    #
    #     pass
    # sede1_string = str(sede1[0]) + "," + str(sede1[1]) + "," + str(sede1[2])

    # print(sede1_string)
    #
    # lista_reparti_sede_1 = cl.getReparti( cl_sock, sede1_string)
    # print(lista_reparti_sede_1)

    # lista_impieghi = cl.getImpieghi(sock_client=cl_sock)
    # print(lista_impieghi)

    # nuovo_dipendente ={"nome": "Mattia", "cognome": "Veroni", "sesso": "M", "data_nascita": "2001-11-24",
    # "luogo":"Via pierino 2", "cf": "GIACMOSPA45945DJ", "data_assunzione": "2020-10-18",
    # "stipendio": "1500.32", "impiego": "Commerciale"}
    #
    # cl.insertDipendente( cl_sock, nuovo_dipendente)

    lista_sedi = cl.getSedi(cl_sock)
    print("listaSedi=",lista_sedi)
    lista_sedi_stringhe = []
    for one_sede in lista_sedi:
        lista_sedi_stringhe.append(str(one_sede))

    #lista_reparti_sede_1=[]

    lista_impieghi = cl.getImpieghi(sock_client=cl_sock)
    print(lista_impieghi)

    def actionListener_Sedi(event):
        sede_scelta = entry_sedi.get()
        sede_scelta_lista = eval(sede_scelta)

        sede1_string = str(sede_scelta_lista[0]) + "," + str(sede_scelta_lista[1]) + "," + str(sede_scelta_lista[2])

        lista_reparti_sede_1 = cl.getReparti(cl_sock, sede1_string)


        # --------------------Reparti-------------------------------
        label_occupation = Label(frame_work, text="Reparti:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=6, column=2, pady=6, padx=3, sticky=W)

        entry_reparti = ttk.Combobox(frame_work, value=lista_reparti_sede_1)
        entry_reparti.grid(row=6, column=3)
        # -----------------------------------------------------------


    # ------------------gender-----
    def get_gender():
        if val.get() == 0:
            return "M"
        else:
            return "F"
    # ------------------------------
    # --------------Get dati -------------------------------------------------
    # nuovo_dipendente ={"nome": "Mattia", "cognome": "Veroni", "sesso": "M", "data_nascita": "2001-11-24",
    # "luogo":"Via pierino 2", "cf": "GIACMOSPA45945DJ", "data_assunzione": "2020-10-18",
    # "stipendio": "1500.32", "impiego": "Commerciale"}
    def datiFrom_create():
        dizionario_dipendenti = {"nome": entry_name.get(), "cognome": entry_surename.get(), "sesso": get_gender(),
                                "data_nascita": entry_dataNascita.get(),
                                "luogo":entry_luogoNascita.get(), "cf": entry_fiscale.get(), "data_assunzione": entry_dateAssunzione.get(),
                                "stipendio": entry_eanrning.get(), "impiego": occupation_menu.get()}
        print(dizionario_dipendenti)

        cl.insertDipendente(cl_sock, dizionario_dipendenti)

    # -------------------------------------------------------
    text = "Add Page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("1020x520")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=75)

    label_title = Label(frame_work, text="Aggiungi Pernosa", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
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
    # ---------------------------GENDER--------------------------
    label_gender = Label(frame_work, text="Sesso:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_gender.grid(row=3, column=0, pady=6, padx=3, sticky=W)

    G = ["M", "F"]
    val = IntVar()
    for i in range(len(G)):
        radio_gender = Radiobutton(frame_work, text=G[i], value=i, variable=val, bg="#801d2b", activeforeground="white",
                                   activebackground="#801d2b", command=get_gender)
        if i == 0:
            radio_gender.grid(row=3, column=1, sticky=W)
        else:
            radio_gender.grid(row=3, column=1, sticky=E)
    # -----------------------------------------------------------
    # -------------------------Birth DATE------------------------------
    label_date = Label(frame_work, text="Data di nascita:", font=("Arial", 14, "normal"), fg="#edb415",
                       bg="#801d2b", )
    label_date.grid(row=4, column=0, pady=6, padx=3, sticky=W)

    entry_dataNascita = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_dataNascita.grid(row=4, column=1)
    # -----------------------------------------------------------
    # --------------------Birth place-----------------------------
    label_occupation = Label(frame_work, text="Luogo di nascita:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=5, column=0, pady=6, padx=3, sticky=W)

    entry_luogoNascita = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_luogoNascita.grid(row=5, column=1)
    # -----------------------------------------------------------
    # -------------------Codice Fiscale-----------------------------
    label_occupation = Label(frame_work, text="Codice Fiscale:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=1, column=2, pady=6, padx=3, sticky=W)

    entry_fiscale = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_fiscale.grid(row=1, column=3)
    # -----------------------------------------------------------
    # --------------------OCCUPATION-----------------------------
    label_occupation = Label(frame_work, text="Impiego:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=2, column=2, pady=6, padx=3, sticky=W)

    occupation_menu = ttk.Combobox(frame_work, value=lista_impieghi, width=10, height=5)
    occupation_menu.grid(row=2, column=3)
    # -----------------------------------------------------------
    # -------------------------DATE------------------------------
    label_date = Label(frame_work, text="Data di assunzione:", font=("Arial", 14, "normal"), fg="#edb415",
                       bg="#801d2b", )
    label_date.grid(row=3, column=2, pady=6, padx=3, sticky=W)

    entry_dateAssunzione = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_dateAssunzione.grid(row=3, column=3)
    # -----------------------------------------------------------

    # ----------------------EARNING------------------------------
    label_eanrning = Label(frame_work, text="Stipendio:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_eanrning.grid(row=4, column=2, pady=6, padx=3, sticky=W)

    entry_eanrning = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_eanrning.grid(row=4, column=3)
    # -----------------------------------------------------------
    # --------------------sedi-------------------------------
    label_occupation = Label(frame_work, text="Sedi:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=5, column=2, pady=6, padx=3, sticky=W)

    entry_sedi = ttk.Combobox(frame_work, value=lista_sedi_stringhe,width=40)
    entry_sedi.grid(row=5, column=3)
    entry_sedi.bind("<<ComboboxSelected>>",actionListener_Sedi)

    # -----------------------------------------------------------




    send = Button(frame_work, text="Add", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, command=datiFrom_create)
    send.grid(row=7, columnspan=5, pady=6, padx=3)

    # Devi farmi un dizionario con tutti i valori interni


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def read_db():  # raad someones data from DB
    def dataFrom_readDB():
        if entry_fiscale.get()=="" or len(entry_fiscale.get())!=16:
            dizionario_ricerca_nome_cognome={"nome": entry_name.get(), "cognome": entry_surename.get()}
        else:
            dizionario_ricerca_read_db = {"nome": entry_name.get(), "cognome": entry_surename.get(),
                                         "codice_fiscale": entry_fiscale.get()}

        data = "this will show the resuslt of a query"
        db_data = Label(frame_work, text=data, font=("Arial", 14, "normal"), fg="#edb415")
        db_data.grid(row=4, columnspan=5, pady=10)

    text = "Read page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("1020x520")
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
    # -------------------Codice Fiscale-----------------------------
    label_occupation = Label(frame_work, text="Codice Fiscale:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=2, columnspan=4, pady=6, padx=3, sticky=W)

    entry_fiscale = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_fiscale.grid(row=2, columnspan=5)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Search", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, command=dataFrom_readDB)
    send.grid(row=3, columnspan=5, pady=6, padx=3)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def update():  # update someones data
    #///////////////////////////////////////////
    def seValueForm():
        # ------------------gender-----
        def get_gender():
            if val.get() == 0:
                return "M"
            else:
                return "F"

        # ------------------------------

        # ------------------------NAME---------------------------
        label_name = Label(frame_work, text="Nome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
        label_name.grid(row=4, column=0, pady=6, padx=3, sticky=W)

        entry_name = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_name.grid(row=4, column=1)
        # -----------------------------------------------------------
        # --------------------SURENAME---------------------------
        label_surename = Label(frame_work, text="Cognome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
        label_surename.grid(row=5, column=0, pady=6, padx=3, sticky=W)

        entry_surename = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_surename.grid(row=5, column=1)
        # -----------------------------------------------------------
        # ---------------------------GENDER--------------------------
        label_gender = Label(frame_work, text="Sesso:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
        label_gender.grid(row=5, column=0, pady=6, padx=3, sticky=W)

        G = ["M", "F"]
        val = IntVar()
        for i in range(len(G)):
            radio_gender = Radiobutton(frame_work, text=G[i], value=i, variable=val, bg="#801d2b",
                                       activeforeground="white",
                                       activebackground="#801d2b", command=get_gender)
            if i == 0:
                radio_gender.grid(row=6, column=1, sticky=W)
            else:
                radio_gender.grid(row=6, column=1, sticky=E)
        # -----------------------------------------------------------
        # -------------------------Birth DATE------------------------------
        label_date = Label(frame_work, text="Data di nascita:", font=("Arial", 14, "normal"), fg="#edb415",
                           bg="#801d2b", )
        label_date.grid(row=7, column=0, pady=6, padx=3, sticky=W)

        entry_dataNascita = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_dataNascita.grid(row=7, column=1)
        # -----------------------------------------------------------
        # --------------------Birth place-----------------------------
        label_occupation = Label(frame_work, text="Luogo di nascita:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=8, column=0, pady=6, padx=3, sticky=W)

        entry_luogoNascita = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_luogoNascita.grid(row=8, column=1)
        # -----------------------------------------------------------
        # -------------------Codice Fiscale-----------------------------
        label_occupation = Label(frame_work, text="Codice Fiscale:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=4, column=2, pady=6, padx=3, sticky=W)

        entry_fiscale = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_fiscale.grid(row=4, column=3)
        # -----------------------------------------------------------
        # --------------------OCCUPATION-----------------------------
        label_occupation = Label(frame_work, text="Impiego:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=5, column=2, pady=6, padx=3, sticky=W)

        occupation_menu = ttk.Combobox(frame_work, value="impiego1 impiego 2 impiego3", width=10, height=5)
        occupation_menu.grid(row=5, column=3)
        # -----------------------------------------------------------
        # -------------------------DATE------------------------------
        label_date = Label(frame_work, text="Data di assunzione:", font=("Arial", 14, "normal"), fg="#edb415",
                           bg="#801d2b", )
        label_date.grid(row=6, column=2, pady=6, padx=3, sticky=W)

        entry_dateAssunzione = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_dateAssunzione.grid(row=6, column=3)
        # -----------------------------------------------------------

        # ----------------------EARNING------------------------------
        label_eanrning = Label(frame_work, text="Stipendio:", font=("Arial", 14, "normal"), fg="#edb415",
                               bg="#801d2b", )
        label_eanrning.grid(row=7, column=2, pady=6, padx=3, sticky=W)

        entry_eanrning = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_eanrning.grid(row=7, column=3)
        # -----------------------------------------------------------
        # --------------------sedi-------------------------------
        label_occupation = Label(frame_work, text="Sedi:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=8, column=2, pady=6, padx=3, sticky=W)

        entry_sedi = ttk.Combobox(frame_work, value="lista sedi", width=40)
        entry_sedi.grid(row=8, column=3)
        # entry_sedi.bind("<<ComboboxSelected>>", actionListener_Sedi)

        # -----------------------------------------------------------
        # --------------------Reparti-------------------------------
        label_occupation = Label(frame_work, text="Reparti:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=9, column=1, pady=6, padx=3, sticky=W)

        entry_reparti = ttk.Combobox(frame_work, value="lista reparti")
        entry_reparti.grid(row=9, column=2)
        # -----------------------------------------------------------

        send = Button(frame_work, text="Update", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                      activeforeground="white",
                      activebackground="#801d2b",
                      pady=10, )
        send.grid(row=10, columnspan=5, pady=6, padx=3)

    # --------------------------------------------------------------------------------------------------------

    #--------------------dictionary from the search of update method----------------
    def get_search():
        if entry_fiscale.get()=="" or len(entry_fiscale.get())!=16:

            dipendente_data = cl.getDipendenteNome( cl_sock, entry_name.get(), entry_surename.get())
            print(dipendente_data)
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            print(nome_reparto)
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )
            print("Ecco le info sulla sede: " + str(info_sede_dipendente) + "  Ed ecco il suo tipo: " + str(type(info_sede_dipendente)))

        else:
            dipendente_data = cl.getDipendenteCf( cl_sock, entry_fiscale.get() )
            print(dipendente_data)
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            print(nome_reparto)
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )
            print("Ecco le info sulla sede: " + str(info_sede_dipendente) + "  Ed ecco il suo tipo: " + str(type(info_sede_dipendente)))

    #////////////////////////////////////////////
    text = "update page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("1020x520")
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
    # -------------------Codice Fiscale-----------------------------
    label_occupation = Label(frame_work, text="Codice Fiscale:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=2, column=1, pady=6, padx=3, sticky=W)

    entry_fiscale = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_fiscale.grid(row=2, column=2)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Search", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, command=lambda:[seValueForm(),get_search()])
    send.grid(row=3, columnspan=5, pady=6, padx=3)

    # request from db
    #data = cl.getExistDipendente()

    # set value on UI
    #seValueForm(frame_work)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def delete():  # delete someone information from db
    def eliminate():
        if messagebox.askokcancel(title="Are you sure", message="delete user?", ):
            print("query to delete usere")
            mess = Label(frame_work, text="user deleted", font=("Arial", 14, "normal"), fg="#edb415")
            mess.grid(row=4, columnspan=5, pady=10)
        else:
            print("option canceld")

    def get_search():
        if entry_fiscale.get()=="" or len(entry_fiscale.get())!=16:
            dizionario_ricerca_nome_cognome={"nome": entry_name.get(), "cognome": entry_surename.get()}
        else:
            dizionario_ricerca_delete = {"nome": entry_name.get(), "cognome": entry_surename.get(),
                                         "codice_fiscale": entry_fiscale.get()}
    text = "Delete page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("1020x520")
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
    # -------------------Codice Fiscale-----------------------------
    label_occupation = Label(frame_work, text="Codice Fiscale:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=2, column=1, pady=6, padx=3, sticky=W)

    entry_fiscale = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_fiscale.grid(row=2, column=2)
    # -----------------------------------------------------------

    send = Button(frame_work, text="Delete", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10,
                  command=lambda :[eliminate(),get_search()])
    send.grid(row=3, columnspan=5, pady=6, padx=3)