# Create: creare nuovi dipendenti e nuove zone associate ai dipendenti tramite l’ID
# Read: leggere dati relativi a zone e/o dipendenti
# Update: modificare le anagrafiche dei dipendenti o delle zone
# Delete: cancellare dati relativi a dipendenti e/o zone.


# i decide to split some Gui code to make it easy to understand
from tkinter import *
from tkinter import messagebox
from AbdulManager.AbdulManager.source import Client as cl
from tkinter import ttk

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def correct_authentication(window, socket_client):

    global cl_sock
    cl_sock = socket_client

    new_window = Tk()
    new_window.title("Work page")
    new_window.geometry("820x460")
    new_window.config(background="#801d2b")

    frame_work = Frame(new_window,
                       bg="#801d2b",
                       )
    frame_work.pack(pady=75)

    label_title = Label(frame_work,
                        text="Ufficio risorse umane", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b", )
    label_title.grid(row=0, columnspan=3, pady=6, padx=6)

    pul_1 = Button(frame_work, text="Create", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command= create,
                   )
    pul_1.grid(row=1, column=0, pady=6, padx=6)

    pul_2 = Button(frame_work, text="Read", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=read_db,
                   )
    pul_2.grid(row=2, column=0, pady=6, padx=6)

    pul_3 = Button(frame_work, text="Update", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=update,
                   )
    pul_3.grid(row=1, column=2, pady=6, padx=6)

    pul_4 = Button(frame_work, text="Delete", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=delete,
                   )
    pul_4.grid(row=2, column=2, pady=6, padx=6)

    pul_5 = Button(frame_work, text="Add Impiegi", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=add_Impieghi,
                   )
    pul_5.grid(row=3, column=0, pady=6, padx=6)

    pul_6 = Button(frame_work, text="Add Sedi", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=add_Sedi,
                   )
    pul_6.grid(row=3, column=2, pady=6, padx=6)

    pul_7 = Button(frame_work, text="Add Reparti", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=add_Reparti,
                   )
    pul_7.grid(row=4, column=0, pady=6, padx=6)

    pul_8 = Button(frame_work, text="Get All dipendenti", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                   activeforeground="white",
                   activebackground="#801d2b",
                   pady=10,
                   command=get_dipendenti,
                   )
    pul_8.grid(row=4, column=2, pady=6, padx=6)

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


    #get activated when reparto is chosen
    def actionListener_reparti(event):
        reparto_scelto = entry_reparti.get()

        global indice_reparto
        for i in range(len(lista_reparti_index)):
            if lista_reparti_index[i][1] == reparto_scelto:
                indice_reparto=lista_reparti_index[i][0]
                break


    # get activated when sede i chosen
    def actionListener_Sedi(event):
        sede_scelta = entry_sedi.get()
        sede_scelta_lista = eval(sede_scelta)
        sede1_string = str(sede_scelta_lista[0]) + "," + str(sede_scelta_lista[1]) + "," + str(sede_scelta_lista[2])

        lista_reparti_sede_1 = cl.getReparti(cl_sock, sede1_string)

        local_index=[]
        lista_reparti_nome=[]
        for i in range(len(lista_reparti_sede_1)):
            temp=eval(lista_reparti_sede_1[i])
            lista_reparti_nome.append(temp[1])
            local_index.append(temp)

            pass

        global lista_reparti_index
        lista_reparti_index=local_index

        # --------------------Reparti-------------------------------
        label_occupation = Label(frame_work, text="Reparti:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=6, column=2, pady=6, padx=3, sticky=W)
        global  entry_reparti
        entry_reparti = ttk.Combobox(frame_work, value=lista_reparti_nome)
        entry_reparti.bind("<<ComboboxSelected>>",actionListener_reparti)
        entry_reparti.grid(row=6, column=3)

        # -----------------------------------------------------------
        pass



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
                                "stipendio": entry_eanrning.get(), "impiego": occupation_menu.get(),
                                "reparto_id": indice_reparto}
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

    label_title = Label(frame_work, text="Aggiungi Persona", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
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
    entry_dataNascita.insert(0,"0000-00-00")
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

    occupation_menu = ttk.Combobox(frame_work, value=lista_impieghi, width=30, height=5)
    occupation_menu.grid(row=2, column=3)
    # -----------------------------------------------------------
    # -------------------------DATE------------------------------
    label_date = Label(frame_work, text="Data di assunzione:", font=("Arial", 14, "normal"), fg="#edb415",
                       bg="#801d2b", )
    label_date.grid(row=3, column=2, pady=6, padx=3, sticky=W)

    entry_dateAssunzione = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_dateAssunzione.insert(0,"0000-00-00")
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

    def get_search():
        if entry_fiscale.get()=="" or len(entry_fiscale.get())!=16:

            dipendente_data = cl.getDipendenteNome( cl_sock, entry_name.get(), entry_surename.get())
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )

            impiego = cl.getInfoImpiego(cl_sock, dipendente_data[7])

            info_totale=[]
            for valore in dipendente_data:
                info_totale.append(valore)

            info_totale.append(nome_reparto)

            for i in range(len(info_sede_dipendente)):
                if i!=0 and i!=4:
                    info_totale.append(info_sede_dipendente[i])
            info_totale.append(impiego[0])
            return info_totale

        else:
            dipendente_data = cl.getDipendenteCf( cl_sock, entry_fiscale.get() )
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )
            impiego = cl.getInfoImpiego(cl_sock, 1)

            info_totale = []
            for valore in dipendente_data:
                info_totale.append(valore)

            info_totale.append(nome_reparto)

            for i in range(len(info_sede_dipendente)):
                if i != 0 and i != 4:
                    info_totale.append(info_sede_dipendente[i])
            info_totale.append(impiego[0])
            return info_totale

    #------------------------------------------------------------------------------------------------------

    def dataFrom_readDB():
        info_totale=get_search()
        info_filterd=[]
        for i in range(len(info_totale)):
            info_totale[i]=str(info_totale[i])
            if not info_totale[i].isdigit():
                info_filterd.append(info_totale[i])

        data = "Nome: "+info_filterd[0]+"\nCognome: "+info_filterd[1]+"\nSesso: "+info_filterd[2]+\
               "\nData di Nascita: "+info_filterd[3]+"\nLuogo di Nascita: "+info_filterd[4]+"\nCodice Fiscale: "+info_filterd[5]+\
               "\nData Assunzione: " + info_filterd[6]+"\nImpiego: "+info_filterd[7]+"\nSede: "+info_filterd[8]+" "+info_filterd[9]+" "+info_filterd[10]+ \
               "\nReparto: " + info_filterd[11]
        db_data = Label(frame_work, text=data, font=("Arial", 14, "normal"), fg="#edb415")
        db_data.grid(row=4, columnspan=5, pady=10)

    text = "Read page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("1020x620")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=75)

    label_title = Label(frame_work, text="Cerca persone", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
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

    def get_search():
        if entry_fiscale.get()=="" or len(entry_fiscale.get())!=16:

            dipendente_data = cl.getDipendenteNome( cl_sock, entry_name.get(), entry_surename.get())
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )

            impiego = cl.getInfoImpiego(cl_sock, dipendente_data[7])
            print("Ecco l'impiego: " + impiego[0])

            info_totale=[]
            for valore in dipendente_data:
                info_totale.append(valore)

            info_totale.append(nome_reparto)

            for i in range(len(info_sede_dipendente)):
                if i!=0 and i!=4:
                    info_totale.append(info_sede_dipendente[i])
            info_totale.append(impiego[0])
            print("info totale ",info_totale)
            return info_totale

        else:
            dipendente_data = cl.getDipendenteCf( cl_sock, entry_fiscale.get() )
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )
            impiego = cl.getInfoImpiego(cl_sock, 1)
            print("Ecco l'impiego: " + impiego[0])

            info_totale = []
            for valore in dipendente_data:
                info_totale.append(valore)

            info_totale.append(nome_reparto)

            for i in range(len(info_sede_dipendente)):
                if i != 0 and i != 4:
                    info_totale.append(info_sede_dipendente[i])
            info_totale.append(impiego[0])
            print("info totale ", info_totale)
            return info_totale

    #------------------------------------------------------------------------------------------------------

    lista_sedi = cl.getSedi(cl_sock)
    lista_sedi_stringhe = []
    for one_sede in lista_sedi:
        lista_sedi_stringhe.append(str(one_sede))

    lista_impieghi = cl.getImpieghi(sock_client=cl_sock)
    print(lista_impieghi)



    def actionListener_reparti(event):
        info_totale=get_search()

        reparto_scelto = entry_reparti_ud.get()

        global indice_reparto_update
       # print("indice prima ",indice_reparto_update)
        for i in range(len(lista_reparti_index_ud)):
            if lista_reparti_index_ud[i][1] == reparto_scelto:

                indice_reparto_update=lista_reparti_index_ud[i][0]

        print("indice dopo ",indice_reparto_update)

    def actionListener_Sedi(event):
        sede_scelta = entry_sedi_ud.get()
        sede_scelta_lista = eval(sede_scelta)
        sede1_string = str(sede_scelta_lista[0]) + "," + str(sede_scelta_lista[1]) + "," + str(sede_scelta_lista[2])

        lista_reparti_sede_1 = cl.getReparti(cl_sock, sede1_string)

        local_index = []
        lista_reparti_nome = []
        for i in range(len(lista_reparti_sede_1)):
            temp = eval(lista_reparti_sede_1[i])
            lista_reparti_nome.append(temp[1])
            local_index.append(temp)

            pass

        lista_reparti_index_ud = local_index

        # --------------------Reparti-------------------------------
        label_occupation = Label(frame_work, text="Reparti:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=9, column=1, pady=6, padx=3, sticky=W)

        entry_reparti_ud = ttk.Combobox(frame_work, value=lista_reparti_nome)
        entry_reparti_ud.bind("<<ComboboxSelected>>",actionListener_reparti)
        entry_reparti_ud.grid(row=9, column=2)
        # -----------------------------------------------------------


    #///////////////////////////////////////////
    def seValueForm():
        info_totale=get_search()

        #funzinamento REPARTI senza richiamare sedi
        sede1_string = str(info_totale[13]) + "," + str(info_totale[14]) + "," + str(info_totale[15])
        lista_reparti_sede_1 = cl.getReparti(cl_sock, sede1_string)
        lista_reparti_nome = []
        local_index = []
        for i in range(len(lista_reparti_sede_1)):
            temp = eval(lista_reparti_sede_1[i])
            lista_reparti_nome.append(temp[1])
            local_index.append(temp)
        global lista_reparti_index_ud
        lista_reparti_index_ud = local_index
        #------------------------------------------------

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
        def datiFrom_update():
            dizionario_dipendenti = {"id":info_totale[0],"nome": entry_name.get(), "cognome": entry_surename.get(),
                                     "sesso": get_gender(),
                                     "data_nascita": entry_dataNascita.get(),
                                     "luogo": entry_luogoNascita.get(), "cf": entry_fiscale.get(),
                                     "data_assunzione": entry_dateAssunzione.get(),
                                     "stipendio": entry_eanrning.get(), "impiego": occupation_menu.get()
                                     ,"reparto_id":indice_reparto_update}
            print(dizionario_dipendenti)

            cl.updateDipendente(cl_sock,dizionario_dipendenti)



        # ------------------------NAME---------------------------
        label_name = Label(frame_work, text="Nome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
        label_name.grid(row=4, column=0, pady=6, padx=3, sticky=W)

        entry_name = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_name.insert(0,info_totale[1])
        entry_name.grid(row=4, column=1)
        # -----------------------------------------------------------
        # --------------------SURENAME---------------------------
        label_surename = Label(frame_work, text="Cognome:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
        label_surename.grid(row=5, column=0, pady=6, padx=3, sticky=W)

        entry_surename = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_surename.insert(0,info_totale[2])
        entry_surename.grid(row=5, column=1)
        # -----------------------------------------------------------
        # ---------------------------GENDER--------------------------
        label_gender = Label(frame_work, text="Sesso:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
        label_gender.grid(row=6, column=0, pady=6, padx=3, sticky=W)

        G = ["M", "F"]
        val = IntVar()
        if info_totale[3]=="M":
            val==0
        else:
            val==1

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
        entry_dataNascita.insert(0,info_totale[4])
        entry_dataNascita.grid(row=7, column=1)
        # -----------------------------------------------------------
        # --------------------Birth place-----------------------------
        label_occupation = Label(frame_work, text="Luogo di nascita:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=8, column=0, pady=6, padx=3, sticky=W)

        entry_luogoNascita = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_luogoNascita.insert(0,info_totale[5])
        entry_luogoNascita.grid(row=8, column=1)
        # -----------------------------------------------------------
        # -------------------Codice Fiscale-----------------------------
        label_occupation = Label(frame_work, text="Codice Fiscale:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=4, column=2, pady=6, padx=3, sticky=W)

        entry_fiscale = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_fiscale.insert(0,info_totale[6])
        entry_fiscale.grid(row=4, column=3)
        # -----------------------------------------------------------
        # --------------------OCCUPATION-----------------------------
        label_occupation = Label(frame_work, text="Impiego:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=5, column=2, pady=6, padx=3, sticky=W)

        occupation_menu = ttk.Combobox(frame_work, value=lista_impieghi, width=35, height=5)
        occupation_menu.insert(0,info_totale[16])
        occupation_menu.grid(row=5, column=3)
        # -----------------------------------------------------------
        # -------------------------DATE------------------------------
        label_date = Label(frame_work, text="Data di assunzione:", font=("Arial", 14, "normal"), fg="#edb415",
                           bg="#801d2b", )
        label_date.grid(row=6, column=2, pady=6, padx=3, sticky=W)

        entry_dateAssunzione = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_dateAssunzione.insert(0,info_totale[8])
        entry_dateAssunzione.grid(row=6, column=3)
        # -----------------------------------------------------------

        # ----------------------EARNING------------------------------
        label_eanrning = Label(frame_work, text="Stipendio:", font=("Arial", 14, "normal"), fg="#edb415",
                               bg="#801d2b", )
        label_eanrning.grid(row=7, column=2, pady=6, padx=3, sticky=W)

        entry_eanrning = Entry(frame_work, font=("Arial", 15), width=15, )
        entry_eanrning.insert(0,info_totale[9])
        entry_eanrning.grid(row=7, column=3)
        # -----------------------------------------------------------
        # --------------------sedi-------------------------------
        label_occupation = Label(frame_work, text="Sedi:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=8, column=2, pady=6, padx=3, sticky=W)

        global entry_sedi_ud
        entry_sedi_ud = ttk.Combobox(frame_work, value=lista_sedi_stringhe, width=40)
        entry_sedi_ud.insert(0,info_totale[13]+" "+info_totale[14]+" "+info_totale[15])
        entry_sedi_ud.grid(row=8, column=3)
        entry_sedi_ud.bind("<<ComboboxSelected>>", actionListener_Sedi)

        # -----------------------------------------------------------
        # --------------------Reparti-------------------------------
        label_occupation = Label(frame_work, text="Reparti:", font=("Arial", 14, "normal"), fg="#edb415",
                                 bg="#801d2b", )
        label_occupation.grid(row=9, column=1, pady=6, padx=3, sticky=W)

        global entry_reparti_ud
        entry_reparti_ud = ttk.Combobox(frame_work,value=lista_reparti_nome)
        entry_reparti_ud.insert(0, info_totale[12])
        entry_reparti_ud.bind("<<ComboboxSelected>>",actionListener_reparti)
        entry_reparti_ud.grid(row=9, column=2)
        global indice_reparto_update
        indice_reparto_update = info_totale[11]
        # -----------------------------------------------------------

        send = Button(frame_work, text="Update", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                      activeforeground="white",
                      activebackground="#801d2b",
                      pady=10,command=datiFrom_update )
        send.grid(row=10, columnspan=5, pady=6, padx=3)

    # --------------------------------------------------------------------------------------------------------

    #--------------------dictionary from the search of update method----------------

    #////////////////////////////////////////////
    text = "update page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("1020x820")
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

    send = Button(frame_work, text="Search", font=("Arial", 12), width=20, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10, command=seValueForm)
    send.grid(row=3, columnspan=5, pady=6, padx=3)



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def delete():  # delete someone information from db

    def eliminate(info_totale):

        if messagebox.askokcancel(title="Are you sure", message="delete user: "+info_totale[1]+" "+info_totale[2]+"  " ):

            cl.deleteDipendente(cl_sock,info_totale[0])

            mess = Label(frame_work, text="user "+info_totale[1]+" "+info_totale[2]+" deleted",
                         font=("Arial", 14, "normal"), fg="#edb415",width=40)
            mess.grid(row=4, columnspan=5, pady=10)
        else:
            mess = Label(frame_work, text="Opzione annullata",
                         font=("Arial", 14, "normal"), fg="#edb415",width=40)
            mess.grid(row=4, columnspan=5, pady=10)

    def get_search():
        if entry_fiscale.get()=="" or len(entry_fiscale.get())!=16:

            dipendente_data = cl.getDipendenteNome( cl_sock, entry_name.get(), entry_surename.get())
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )

            impiego = cl.getInfoImpiego(cl_sock, dipendente_data[7])
            print("Ecco l'impiego: " + impiego[0])

            info_totale=[]
            for valore in dipendente_data:
                info_totale.append(valore)

            info_totale.append(nome_reparto)

            for i in range(len(info_sede_dipendente)):
                if i!=0 and i!=4:
                    info_totale.append(info_sede_dipendente[i])
            info_totale.append(impiego[0])
            print("info totale ",info_totale)

            eliminate(info_totale)

        else:
            dipendente_data = cl.getDipendenteCf( cl_sock, entry_fiscale.get() )
            info_reparto_dipendente= cl.getInfoReparto( cl_sock, dipendente_data[11] )
            nome_reparto = info_reparto_dipendente[0]
            info_sede_dipendente = cl.getInfoSede( cl_sock, info_reparto_dipendente[1] )
            impiego = cl.getInfoImpiego(cl_sock, 1)
            print("Ecco l'impiego: " + impiego[0])

            info_totale = []
            for valore in dipendente_data:
                info_totale.append(valore)

            info_totale.append(nome_reparto)

            for i in range(len(info_sede_dipendente)):
                if i != 0 and i != 4:
                    info_totale.append(info_sede_dipendente[i])
            info_totale.append(impiego[0])
            print("info totale ", info_totale)
            eliminate(info_totale)

    #------------------------------------------------------------------------------------------------------

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
                  command=get_search)
    send.grid(row=3, columnspan=5, pady=6, padx=3)

#///////////////////////////////////////////////////////////////////////////////////////

def add_Impieghi():

    def Nuovo_impiego():
        impiego=entry_impiego.get()
        cl.insertImpiego(cl_sock,str(impiego))

    text = "Add page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("420x320")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=50)

    label_title = Label(frame_work, text="Add Impiego", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=2, pady=6, padx=6)

    # ------------------------NAME---------------------------
    label_name = Label(frame_work, text="Nuovo Ipiego:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_name.grid(row=1, column=0, pady=6, padx=3, sticky=W)

    entry_impiego = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_impiego.grid(row=1, column=1)
    # -----------------------------------------------------------

    send = Button(frame_work, text="ADD", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10,
                  command=Nuovo_impiego)
    send.grid(row=2, columnspan=2, pady=6, padx=3)


#---------------------------------------------------------------------------------------------------------------------------
def add_Sedi():

    def Nuova_sede():
        dizionario_Nuova_Sede={"indirizzo":entry_indirizzo.get(),"citta":entry_citta.get(),"provincia":entry_provincia.get(),
                               "cap":entry_cap.get()}

        cl.insertSede(cl_sock,dizionario_Nuova_Sede)

    text = "Add page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("420x420")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=50)

    label_title = Label(frame_work, text="Nuovo Sede", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=2, pady=6, padx=6)

    # ------------------------Indirizzo---------------------------
    label_indirizzo = Label(frame_work, text="Indirizzo:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_indirizzo.grid(row=1, column=0, pady=6, padx=3, sticky=W)

    entry_indirizzo = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_indirizzo.grid(row=1, column=1)
    # -----------------------------------------------------------
    # ------------------------Citta---------------------------
    label_citta = Label(frame_work, text="Citta:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_citta.grid(row=2, column=0, pady=6, padx=3, sticky=W)

    entry_citta = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_citta.grid(row=2, column=1)
    # -----------------------------------------------------------
    # ------------------------Provincia---------------------------
    label_provincia = Label(frame_work, text="Provincia:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_provincia.grid(row=3, column=0, pady=6, padx=3, sticky=W)

    entry_provincia = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_provincia.grid(row=3, column=1)
    # -----------------------------------------------------------
    # ------------------------CAP--------------------------
    label_cap = Label(frame_work, text="Cap:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_cap.grid(row=4, column=0, pady=6, padx=3, sticky=W)

    entry_cap = Entry(frame_work, font=("Arial", 15), width=15, )
    entry_cap.grid(row=4, column=1)
    # -----------------------------------------------------------

    send = Button(frame_work, text="ADD", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10,
                  command=Nuova_sede)
    send.grid(row=5, columnspan=2, pady=6, padx=3)


#-----------------------------------------------------------------------------------------------------------------------
def add_Reparti():

    lista_sedi = cl.getSedi(cl_sock)
    lista_sedi_stringhe = []
    for one_sede in lista_sedi:
        lista_sedi_stringhe.append(str(one_sede))

    def get_sede(event):
        sede_scelta=eval(entry_sedi.get())
        print("sede  scelta",type(sede_scelta))

        global id_sede
        id_sede=cl.get_id_sede(cl_sock,sede_scelta)


    def Nuovo_reparto():
        diz_nuovo_reparto={"nome_reparto":entry_reparto.get(),"id_sede":id_sede}

        cl.insertReparto(cl_sock,diz_nuovo_reparto)

    text = "Add page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("420x320")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=50)

    label_title = Label(frame_work, text="Nuovo Reparto", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=2, pady=6, padx=6)

    # --------------------sedi-------------------------------
    label_occupation = Label(frame_work, text="Sedi:", font=("Arial", 14, "normal"), fg="#edb415",
                             bg="#801d2b", )
    label_occupation.grid(row=1, column=0, pady=6, padx=3, sticky=W)


    entry_sedi = ttk.Combobox(frame_work, value=lista_sedi_stringhe, width=40)
    entry_sedi.grid(row=1, column=1)
    entry_sedi.bind("<<ComboboxSelected>>",get_sede)

    # -----------------------------------------------------------
    # ------------------------Nuovo reparto---------------------------
    label_reparto = Label(frame_work, text="Nuovo Reparto:", font=("Arial", 14, "normal"), fg="#edb415", bg="#801d2b", )
    label_reparto.grid(row=2, column=0, pady=6, padx=3, sticky=W)

    entry_reparto = Entry(frame_work, font=("Arial", 15), width=23)
    entry_reparto.grid(row=2, column=1)
    # -----------------------------------------------------------

    send = Button(frame_work, text="ADD", font=("Arial", 12), width=10, fg="#edb415", bg="#801d2b",
                  activeforeground="white",
                  activebackground="#801d2b",
                  pady=10,
                  command=Nuovo_reparto)
    send.grid(row=3, columnspan=2, pady=6, padx=3)

def get_dipendenti():

    text = "Get page"
    Window_create = Tk()
    Window_create.title(text)
    Window_create.geometry("420x1020")
    Window_create.config(background="#801d2b")

    frame_work = Frame(Window_create, bg="#801d2b", )
    frame_work.pack(pady=50)

    label_title = Label(frame_work, text="Tutti i Dipendenti", font=("Arial", 20, "normal"), fg="#edb415", bg="#801d2b")
    label_title.grid(row=0, columnspan=2, pady=6, padx=6)

    tutti_dipendenti=eval(cl.get_all_dipendenti(cl_sock))

    print("prova--",tutti_dipendenti[1])



    pos=1
    for i in tutti_dipendenti:
        data = "Nome: " + str(i[1]) + "\nCognome: " + i[2] + "\nSesso: " + i[3] + \
               "\nData di Nascita: " + i[4] + "\nLuogo di Nascita: " + i[5] + "\nCodice Fiscale: " + \
               i[6] + "\nData Assunzione: " + i[8] + "\nStiprndio:"+str(i[9])

        db_data = Label(frame_work, text=data, font=("Arial", 14, "normal"), fg="#edb415",width=35)
        db_data.grid(row=pos,pady=10)
        print(pos)
        pos=pos+1
