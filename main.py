from tkinter import *

def App():

    #Basic Application Setup
    root = Tk()
    root.title("InboxIn")
    root.geometry("700x600")
    root.grid()
    logo = PhotoImage(file="./resources/InboxIn Logo.png")
    root.iconphoto(False , logo)
    root.resizable(False , False)

    #Logo In Window
    logolable = Label(image=logo)
    logolable.grid(row=0 , column=1)

    #Label Collection

    spanlable = Label(text="                               ")
    spanlable.grid(row=0 , column= 0)


    filelabel = Label(text="Email File: ")#Email File: Label
    filelabel.grid(row=2 , column=0)


    root.mainloop()

if __name__ == "__main__":
    App()