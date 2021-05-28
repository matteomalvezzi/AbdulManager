from tkinter import *
from tkinter import messagebox

from AbdulManager.AbdulManager.source import Client, Gui_interface_dbAction


# Show message log box
def show_message_box(messagge_text):
    messagebox.showerror("Application", str(messagge_text))

def gui( client_sock ):
    # Authentication method
    def check(user, password, window):

        #Check login
        result_of_login = Client.send_password_to_server(user, password, client_sock)

        #Check result of login
        if result_of_login:
            Gui_interface_dbAction.correct_authentication(window, client_sock)
        else:
            print("Authentication error")

    def read():#button main function that call check()
        user = entry_1.get()
        passw = entry_2.get()
        check(user,passw,window)

    window = Tk()  # istance my window

    window.geometry("520x420")  # some Stytle
    window.title("Login Page")
    window.config(background="#5a5050")

    icon = PhotoImage(file="../resource/pngegg.png")  # convert my img and set logo
    window.iconphoto(True, icon)
    icon_2 = PhotoImage(file="../resource/green_icon.png")


    # create the mian frame
    frame = Frame(window,
                  bg="#5a5050",
                  )
    frame.pack(pady=65)
    # create my first label and add some style
    label_1 = Label(frame,
                    image=icon_2,
                    bg="#5a5050",
                    compound=TOP).grid(row=0, columnspan=2, pady=6)

    label_name = Label(frame,
                       text="Username",
                       font=("SimHei", 15, "normal"),
                       fg="#a2d4ab", bg="#5a5050",
                       ).grid(row=1, column=0, pady=4, sticky=W,padx=2)
    # create the fist entry box
    entry_1 = Entry(frame,
                    font=("SimHei", 15),
                    width=15,
                    fg="#a2d4ab",
                    )
    entry_1.grid(row=1, column=1)

    label_pass = Label(frame,
                       text="Password",
                       font=("SimHei", 15,),
                       fg="#a2d4ab", bg="#5a5050",
                       ).grid(row=2, column=0, pady=2, sticky=W,padx=2)

    # create the seconde entry box
    entry_2 = Entry(frame,
                    font=("SimHei", 15),
                    show="*",
                    fg="#a2d4ab",
                    width=15,
                    )
    entry_2.grid(row=2, column=1)

    # create my button and ad sone style
    button = Button(frame,
                    text="Login",
                    font=("SimHei", 20),
                    fg="#a2d4ab",
                    bg="#5a5050",
                    width=7,
                    activeforeground="white",
                    activebackground="#5a5050",
                    pady=10,
                    command=read)

    button.grid(row=3, columnspan=2, pady=6)

    window.mainloop()  # make sure that my window is visible

