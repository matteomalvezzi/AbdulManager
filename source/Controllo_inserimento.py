
#=================================================THIS PYTHON FILE IS FOR INPUT CHECKS=====================

#check data before adding to the DATABASE

def check_create(nome,cognome,data_nascita,luogo_nascita,codice_fiscale,impiego,data_assunzione,stipendio,sedi):
    #-----if name or surenaem or luogo di nascita or contain numbers---------
    flag_nome=False
    for i in nome:
        if i.isdigit():
            flag_nome=True

    flag_cognome=False
    for i in cognome:
        if i.isdigit():
            flag_cognome=True

    flag_luogoNascita = False
    for i in luogo_nascita:
        if i.isdigit():
            flag_luogoNascita = True
    #---------------------------------------------

    #-------data di nascita-----data di assunzione-----
    flag_dataNascita=False
    for i in data_nascita:
        if i.isalpha():
            flag_dataNascita=True


    flag_dataAssunzione=False
    for i in data_assunzione:
        if i.isalpha():
            flag_dataAssunzione=True

    #--------------------------------------------------


# def ciao(data):
#     for i in data:
#         if i.isalpha():
#             print("carattere==",i)
#         else:
#             print("numero o altro==",i)
#
# ciao("2010-06-15")