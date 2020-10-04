from tkinter import *
from tkinter import scrolledtext
import time
from cryptography.fernet import Fernet
from tkinter import filedialog


#Funciones
def close_window(): 
    window.destroy()

def cryptfunc(f):

    key = Fernet.generate_key()
    f = Fernet(key)
    llave = open("llave", "w")
    llave.write(key)

    memoria = open("memoria","w")

    token = f.encrypt(variable.encode("utf-8"))
    global tokenglobal
    tokenglobal = token
    
    txt.delete('1.0', END)
    txt.insert(INSERT,token)
    
    global file_path
    print(file_path)   
    nombreencript=file_path.rsplit('\\', 1)[-1].rsplit('.',1)[0]+"_C.txt"
    
    #Escribes el hash en el fichero
    memoria.write(nombreencript)
    cryptfile = open(nombreencript, "w")
    cryptfile.write(token.decode("utf-8"))
    cryptfile.close()


def decryptfunc(f):
    txt.delete('1.0', END)
    txt.insert(INSERT,f.decrypt(tokenglobal))   

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




tokenglobal = 0
variable = ""
file_path = ""


#GUI
txt = scrolledtext.ScrolledText(window,width=88,height=15, background = '#41484f', foreground = "white",relief=FLAT)
close_window= Button(window, text = "X",font=("Helvetica", 16), bg='#2B2D2F',foreground="#47474A",highlightthickness=0,relief=FLAT,command = close_window)
lbl         = Label (window, text="Welcome to my crypto app", font=("Helvetica", 16),bg='#2B2D2F',foreground="white")
lbl2        = Label (window, text="Aguilar Pacheco Kevin David", font=("Helvetica", 6),bg='#2B2D2F',foreground="white")
lbl3        = Label (window, text="Practica 0", font=("Helvetica", 6),bg='#2B2D2F',foreground="white")
crypt       = Button(window, text="Crypt", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID, foreground="#B5B1BA", command=lambda: cryptfunc(f))
decrypt     = Button(window, text="Decrypt", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:decryptfunc(f))
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


txt.insert(INSERT,variable)

window.mainloop()
