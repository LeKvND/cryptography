from tkinter import *
from tkinter import scrolledtext
import time
from cryptography.fernet import Fernet
from tkinter import filedialog
import os.path

#Funciones
def close_window(): 
    window.destroy()

def cryptfunc():
    global f
    
    key = Fernet.generate_key()
    llave = open("llave", "w")
    llave.write(key.decode("utf-8"))
    llave.close()


    f = Fernet(key)

    token = f.encrypt(variable.encode("utf-8"))

    
    txt.delete('1.0', END)
    txt.insert(INSERT,token)
    
    global file_path
    nombreencript=file_path.rsplit('\\', 1)[-1].rsplit('.',1)[0]+"_C.txt"
    
    memoria = open("memoria.txt", "w")    
    memoria.write(nombreencript)
    memoria.close()

    cryptfile = open(nombreencript, "w")
    cryptfile.write(token.decode("utf-8"))
    cryptfile.close()


def decryptfunc():

    llavefernet = open("llave", "r")
    key = llavefernet.read().encode("utf-8")
    llavefernet.close()

    memoria = open("memoria.txt", "r")
    archivoaleer = memoria.read()
    memoria.close()


    textoencrypt = open(archivoaleer, "r")
    textoadecrypt = textoencrypt.read()
    textoencrypt.close()

    global f
    f = Fernet(key)
    txt.delete('1.0', END)
    txt.insert(INSERT,f.decrypt(textoadecrypt.encode("utf-8")))

    nombredecrypt=archivoaleer.rsplit('.',1)[0].rsplit('_',1)[0]+"_D.txt"
    decryptfile = open(nombredecrypt, "w")
    decryptfile.write(f.decrypt(textoadecrypt.encode("utf-8")).decode("utf-8"))
    decryptfile.close()
   

def filefunc():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text files",".txt")])
    fichero = open(file_path, "r")
    
    global variable
    variable=fichero.read()

    txt.delete('1.0', END)
    txt.insert(INSERT,variable)
    

##############






#Creacion interfaz
window = Tk()
window.title("Practica 0")
window.geometry("700x400+100+300")
window.configure(bg='#2B2D2F')
window.overrideredirect(1)



##Generar llave


llaveinicio = Fernet.generate_key()
f = Fernet(llaveinicio)
tokenglobal = 0
variable = ""
file_path = ""







#GUI
txt = scrolledtext.ScrolledText(window,width=88,height=15, background = '#41484f', foreground = "white",relief=FLAT)
close_window= Button(window, text = "X",font=("Helvetica", 16), bg='#2B2D2F',foreground="#47474A",highlightthickness=0,relief=FLAT,command = close_window)
lbl         = Label (window, text="Welcome to my crypto app", font=("Helvetica", 16),bg='#2B2D2F',foreground="white")
lbl2        = Label (window, text="Aguilar Pacheco Kevin David", font=("Helvetica", 6),bg='#2B2D2F',foreground="white")
lbl3        = Label (window, text="Practica 0", font=("Helvetica", 6),bg='#2B2D2F',foreground="white")
crypt       = Button(window, text="Crypt", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID, foreground="#B5B1BA", command=lambda: cryptfunc())
decrypt     = Button(window, text="Decrypt", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:decryptfunc())
filechooser = Button(window, text="Choose File", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:filefunc())

#Places
txt.place(x=-2, y=260, anchor="w")
lbl.place(x=350, y=20, anchor="center")
lbl2.place(x=55, y=390, anchor="center")
lbl3.place(x=675, y=390, anchor="center")
crypt.place(x=500, y=70, anchor="w")
decrypt.place(x=580, y=70, anchor="w")
filechooser.place(x=10, y=70, anchor="w")
close_window.place(x=670, y=2)


window.mainloop()
