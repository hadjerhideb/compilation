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


for i in range(0, len(H)) :
        if ltr(H[i]) and ltr(H[i+1]):
            s+=H[i]

        elif let(H[i])     :

            if( H[i+1]=='+'and  H[i+2]=='+' ) or ( H[i+1]=='-' and
H[i+2]=='-') or (H[i+1]==' ') or (ope (H[i+1]) ) :
                 s+=H[i]+'#'
            elif  nem(H[i+1]) or(H[i+1]=='_') :
                   s+=H[i]
            else :
                    s+=H[i]
        elif nem (H[i]) :
             if H[i+1]=='.' or let (H[i+1]):

                 s+=H[i]
             elif H[i+1]==' ':
                 s+=H[i]+'#'
             elif ope(H[i+1]):
                   s+=H[i]+'#'
             else:
                    s+=H[i]
        elif ope(H[i]):

             if    (H[i]=='+'and H[i+1]=='+') or (H[i]=='-'and
H[i+1]=='-') or ((H[i]=='<'or'>'or'='or'!'or ':') and (H[i+1]=='=' and
(nem(H[i+2]) or ope (H[i+2]) or let(H[i+2])) )) or (H[i]=='.' and
nem(H[i+1])) or(H[i]=='_' and nem(H[i+1])) or((H[i]=='+' or
H[i]=='-')and H[i+1]=='.'and nem (H[i+2])) or(nem(H[i-1])and
H[i]=='.'and nem(H[i+1])):
                    s+= H[i]
             elif ((H[i-2]=='+'and H[i-1]=='+'and H[i]=='+')or
(H[i-2]=='-'and H[i-1]=='-'and H[i]=='-')) or((ope (H[i-1]) or let
(H[i-1]))and (H[i]=='+'or H[i]=='-') and nem (H[i+1]) ) or     ((ope
(H[i-1]) or let (H[i-1]))and (H[i]=='+'or H[i]=='-') and
H[i+1]=='.'and nem (H[i+2])) :
                   s+='#'+H[i]

             elif (H[i]=='+'and H[i+1]!='+') or (H[i]=='-'and H[i+1]!='-'):
                s+= H[i] +'#'


             elif (H[i+1==' '])or (nem (H[i+1])or let (H[i+1])) :
                s+=H[i]+'#'
             else:
               s+=H[i]
    s+='#'
           
        
        
# ================================================================================================
T=( [15,10,20, 7, 2, 5, 3, 1, 1, 3,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1, 4,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1, 6,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1, 7,-1,-1,-1, 8,-1,-1,-1],
        [-1,-1,-1, 9,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1, 9,-1,-1,-1,-1,-1,-1,-1],
        [-1,11,-1,12,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,12,-1,-1,-1,13,-1,-1,-1],
        [-1,-1,-1,14,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,14,-1,-1,-1,-1,-1,-1,-1],
        [16,-1,-1,17,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,17,-1,-1,-1,18,-1,-1,-1],
        [-1,-1,-1,19,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,19,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,20,20,-1,-1,-1,-1,-1,-1,21],
        [-1,-1,20,20,-1,-1,-1,-1,-1,-1,22],
        [-1,-1,20,20,-1,-1,-1,-1,-1,-1,23],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,22],

    )
    ent2.delete("1.0","end")
    i=0
    z=''
    k=''
    ec=0

    while i < (len(s)):
        tc=s[i]
        if type(tc) != 100:
            z=z+s[i]
            if ec != -1 and type(tc)!=-1:

                print(T[ec][type(tc)])
                ec=T[ec][type(tc)]
        else:

            if ec==1 :  k=k+" "+z+"  : est une separateur  ' ( )  [ ]
{ } ; .' \n"
            elif ec==2 :  k=k+" "+z+"  : est une operateur  *  / \n "
            elif ec==3 :  k=k+" "+z+"  : est une operateur <  > = \n"
            elif ec==4 :  k=k+" "+z+"  : est une operateur '== ' '<=' '>='\n "
            elif ec==5 :  k=k+" "+z+"  : est  une seperateur  ! : \ \n"
            elif ec==6 :  k=k+" "+z+"  : est une operateur  != :=  \n "
            elif ec==7 :  k=k+" "+z+"  : est nombre entier \n"
            elif ec==9 :  k=k+" "+z+"  : est nombre real \n"
            elif ec==11 : k=k+" "+z+" : est pas negatif \n"
            elif ec==12 : k=k+" "+z+" : est nombre entier signe  negatif \n "
            elif ec==14 : k=k+" "+z+" : est nombre real signe negatif  \n "
            elif ec==16 : k=k+" "+z+" : est pas positif \n"
            elif ec==17 : k=k+" "+z+" : est nombre entier signe  positif \n "
            elif ec==19 : k=k+" "+z+" : est nombre real signe positif  \n "
            elif ec==20 : k=k+" "+z+" : est nombres ou letteres ou les
deux avec '_' \n "
            elif ec==15 : k=k+" "+z+" : is operateur positif \n"
            elif ec==10 : k=k+" "+z+" : is operateur negatif \n"
            else :        k=k+" "+z+" : is the erreur \n "
            z= ''
            ec =0
        i=i+1



    ent2.insert(END,k)
   
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
