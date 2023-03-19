from cgitb import text
import tkinter
from tkinter import *
from tkinter import END
from tkinter import filedialog
from tkinter.messagebox import askokcancel
from tkinter import filedialog as fd
from tkinter.filedialog import FileDialog, asksaveasfile

# ===========================================================================================
window = Tk()
window.geometry('800x500')
window.title("Tp comp")
#============================================================================================
def qlic():
    ent2.config(state='disable')

# =============================================================================================
def quit():
    response = askokcancel("quit", "هل تريد تسجيل الخروج")
    print(response)
    if response:
        window.destroy()


# ===========================================================================================
def open():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')

    )
    f = fd.askopenfile(filetypes=filetypes)
    ent.insert('1.0', f.readlines())


# ================================================================================================
def save():
    file = ent.get("1.0", END)
    fob = filedialog.asksaveasfile(filetypes=(
        ('text files', '*.txt'),
        ('All files', '*.*')
    ))
    try:
        fob.write(file)
        fob.close()

        ent.update()
        fob.config(text="saved")
        fob.after(3000, lambda: b1.config(text='save'))
    except:
        print("there is an error...")


# ================================================================================================
menuber = Menu(window)
window.config(menu=menuber)
# ===========================================================================================
fileMenu = Menu(menuber, tearoff=0)
menuber.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open)
fileMenu.add_command(label="Save", command=lambda: save())
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)
# =========================================================================================
editMenu = Menu(menuber, tearoff=0)
menuber.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Analyse")
editMenu.add_command(label="Santaxique")
editMenu.add_separator()
editMenu.add_command(label="Semantaxique")

# ============================================================================================
op = tkinter.Frame(master=window)
op.grid(row=0, column=0, padx=40)
ent = tkinter.Text(master=window)
ent.grid(row=0, column=0)
# ============================================================================================
op1 = tkinter.Frame(master=window)
op1.grid(row=0, column=4, padx=40)
ent2 = tkinter.Text(master=window)
ent2.grid(row=0, column=4)

window.mainloop()