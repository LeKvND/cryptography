from Crypto.Cipher import DES
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import os.path
from PIL import ImageTk, Image

llave = ""
key = b'default1'
iv = b'skzlkpoi'
des  = DES.new(key, DES.MODE_ECB)
des1 = DES.new(key, DES.MODE_CBC, iv)
des2 = DES.new(key, DES.MODE_CFB, iv)
des3 = DES.new(key, DES.MODE_OFB, iv) 
aux=b''

filename=""
def close_window(): 
    window.destroy()

def filefunc():
    global filename
    filename = filedialog.askopenfilename()
    img = ImageTk.PhotoImage(Image.open(filename)) 
    # reading the image 
    panel.configure(image = img)
    panel.image = img 
        

def ECB_cifrar():
    global filename
    global key 
    global iv
    global des
    ##ECB
    print(key)
    image = open(filename,"rb")
    nombreencript=filename.rsplit('.',1)[0]+"_ECB.bmp"
    new_image = open(nombreencript,"wb")
    new_image.write(image.read(54))
    bytes_to_encrypt = image.read()
    new_image.write(des.encrypt(bytes_to_encrypt))
    img = ImageTk.PhotoImage(Image.open(nombreencript)) 
    panel1.configure(image = img)
    panel1.image = img
    print(key)


def ECB_decifrar():
    global filename
    global key 
    global iv
    global des
    print(key)
    image = open(filename,"rb")
    nombredecript=filename.rsplit('.',1)[0]+"_DES.bmp"
    new_image = open(nombredecript,"wb")
    new_image.write(image.read(54))
    bytes_to_decrypt = image.read()
    new_image.write(des.decrypt(bytes_to_decrypt))
    img = ImageTk.PhotoImage(Image.open(nombredecript)) 
    panel1.configure(image = img)
    panel1.image = img 
    print(key)


def CBC_cifrar():
    global filename
    global key 
    global iv
    global des
    ##CBC
    image = open(filename,"rb")
    nombreencript=filename.rsplit('.',1)[0]+"_CBC.bmp"
    new_image = open(nombreencript,"wb")
    new_image.write(image.read(54))
    bytes_to_encrypt = image.read()
    new_image.write(iv + des1.encrypt(bytes_to_encrypt))
    img = ImageTk.PhotoImage(Image.open(nombreencript)) 
    panel1.configure(image = img)
    panel1.image = img 

def CBC_decifrar():
    global filename
    global key 
    global iv
    global des
    image = open(filename,"rb")
    nombredecript=filename.rsplit('.',1)[0]+"_DES.bmp"
    new_image = open(nombredecript,"wb")
    new_image.write(image.read(54))
    bytes_to_decrypt = image.read()
    aux = des1.decrypt(bytes_to_decrypt)
    new_image.write(aux[8:])
    img = ImageTk.PhotoImage(Image.open(nombredecript)) 
    panel1.configure(image = img)
    panel1.image = img 



def CFB_cifrar():
    global filename
    global key 
    global iv
    global des
    ##CFB
    image = open(filename,"rb")
    nombreencript=filename.rsplit('.',1)[0]+"_CFB.bmp"
    new_image = open(nombreencript,"wb")
    new_image.write(image.read(54))
    bytes_to_encrypt = image.read()
    new_image.write(iv + des2.encrypt(bytes_to_encrypt))
    img = ImageTk.PhotoImage(Image.open(nombreencript)) 
    panel1.configure(image = img)
    panel1.image = img

def CFB_decifrar():
    global filename
    global key 
    global iv
    global des
    image = open(filename,"rb")
    nombredecript=filename.rsplit('.',1)[0]+"_DES.bmp"
    new_image = open(nombredecript,"wb")
    new_image.write(image.read(54))
    bytes_to_decrypt = image.read()
    aux = des2.decrypt(bytes_to_decrypt)
    new_image.write(aux[8:])
    img = ImageTk.PhotoImage(Image.open(nombredecript)) 
    panel1.configure(image = img)
    panel1.image = img 

def OFB_cifrar():
    global filename
    global key 
    global iv
    global des
    global aux
    ##OFB
    image = open(filename,"rb")
    nombreencript=filename.rsplit('.',1)[0]+"_OFB.bmp"
    new_image = open(nombreencript,"wb")
    new_image.write(image.read(54))
    bytes_to_encrypt = image.read()
    aux = iv + des3.encrypt(bytes_to_encrypt)
    new_image.write(aux)
    img = ImageTk.PhotoImage(Image.open(nombreencript)) 
    panel1.configure(image = img)
    panel1.image = img

def OFB_decifrar():
    global filename
    global key 
    global iv
    global des
    global aux
    decCipher = DES.new(key, DES.MODE_OFB, aux[:DES.block_size])
    image = open(filename,"rb")
    nombredecript=filename.rsplit('.',1)[0]+"_DES.bmp"
    new_image = open(nombredecript,"wb")
    new_image.write(image.read(54))
    bytes_to_decrypt = image.read()
    aux = decCipher.decrypt(bytes_to_decrypt[DES.block_size:])
    new_image.write(aux)
    img = ImageTk.PhotoImage(Image.open(nombredecript)) 
    panel1.configure(image = img)
    panel1.image = img 

def cargar_llave(llave):
    global key
    global des
    global des1
    global des2
    global des3
    global iv
    key = llave.get().encode('utf-8')
    print(key)
    des  = DES.new(key, DES.MODE_ECB)
    des1 = DES.new(key, DES.MODE_CBC, iv)
    des2 = DES.new(key, DES.MODE_CFB, iv)
    des3 = DES.new(key, DES.MODE_OFB, iv) 


#interfaz
window = Tk()
window.title("Practica 3")
window.geometry("1150x630+100+300")
window.configure(bg='#2B2D2F')

canvas2 = Canvas(window, width = 500, height = 500)    
close_window= Button(window, text = "X",font=("Helvetica", 16), bg='#2B2D2F',foreground="#47474A",highlightthickness=0,relief=FLAT,command = close_window)
lbl         = Label (window, text="CIFRADOR DES", font=("Helvetica", 16),bg='#2B2D2F',foreground="white")
lbl2        = Label (window, text="Equipo 2", font=("Helvetica", 9),bg='#2B2D2F',foreground="white")
lbl3        = Label (window, text="Practica DES", font=("Helvetica", 9),bg='#2B2D2F',foreground="white")
lbl4        = Label (window, text="Inserta tu key:", font=("Helvetica", 15),bg='#2B2D2F',foreground="white")
llave       = ttk.Entry(window)
cargarllave    = Button(window, text="Cargar LLave", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID, foreground="#B5B1BA",command=lambda:cargar_llave(llave))

cryptECB    = Button(window, text="CryptECB", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID, foreground="#B5B1BA",command=lambda:ECB_cifrar())
cryptCBC    = Button(window, text="CryptCBC", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID, foreground="#B5B1BA",command=lambda:CBC_cifrar())
cryptCFB    = Button(window, text="CryptCFB", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID, foreground="#B5B1BA",command=lambda:CFB_cifrar())
cryptOFB    = Button(window, text="CryptOFB", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID, foreground="#B5B1BA",command=lambda:OFB_cifrar())
decryptECB     = Button(window, text="DecryptECB", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:ECB_decifrar())
decryptCBC     = Button(window, text="DecryptCBC", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:CBC_decifrar())
decryptCFB     = Button(window, text="DecryptCFB", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:CFB_decifrar())
decryptOFB     = Button(window, text="DecryptOFB", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:OFB_decifrar())

filechooser = Button(window, text="Choose File", font=("Helvetica", 16),bg='#2B2D2F',relief=SOLID,foreground="#B5B1BA",command=lambda:filefunc())


#Places
lbl4.place(x=470, y=70, anchor="center")
llave.place(x=600, y=70, anchor="center")
cargarllave.place(x=740, y=70, anchor="center")
lbl.place(x=580, y=20, anchor="center")
lbl2.place(x=40, y=620, anchor="center")
lbl3.place(x=1100, y=620, anchor="center")
cryptECB.place(x=530, y=120, anchor="w")
cryptCBC.place(x=530, y=220, anchor="w")
cryptCFB.place(x=530, y=320, anchor="w")
cryptOFB.place(x=530, y=420, anchor="w")
decryptECB.place(x=520, y=160, anchor="w")
decryptCBC.place(x=520, y=260, anchor="w")
decryptCFB.place(x=520, y=360, anchor="w")
decryptOFB.place(x=520, y=460, anchor="w")
filechooser.place(x=10, y=60, anchor="w")
close_window.place(x=1110, y=2)

# loading the image 
img = ImageTk.PhotoImage(Image.open("default.jpg")) 
  
# reading the image 
panel = Label(window, image = img) 
panel1 = Label(window, image = img) 
  
# setting the application 
panel.place(x=10, y=100) 
panel1.place(x=640, y=100) 
  

window.mainloop()