from tkinter import Tk, Button, Frame, messagebox, simpledialog, Label, Entry, ttk
from xml.dom import ValidationErr
from Datos import *;

ventana = Tk()
ventana.title('Inicio de sesión - Practica 12')
ventana.geometry('300x400')

seccionCorreo = Frame(ventana, bg='#EBEBEB')
seccionCorreo.pack(expand = True, fill='both')

seccionContraseña = Frame(ventana, bg='#EBEBEB')
seccionContraseña.pack(expand = True, fill='both')

seccionBoton = Frame(ventana, bg='#EBEBEB')
seccionBoton.pack(expand = True, fill='both')

solicitudCorreo = Label(seccionCorreo, text='Ingrese su correo: ')
solicitudCorreo.place(x=50, y=50)
correoP = ttk.Entry(seccionCorreo)
correoP.place(x=150, y=50)

solicitudContraseña = Label(seccionContraseña, text='Ingrese su contraseña: ')
solicitudContraseña.place(x=25, y=50)
contraseñaP = ttk.Entry(seccionContraseña, show='*')
contraseñaP.place(x=150, y=50)

corr = '121037801@upq.edu.mx'
cont = '121037801'


validacion = Datos(correoP, contraseñaP, corr, cont)

botonValidar = Button(seccionBoton, text='Iniciar sesión', command = validacion.Validar)
botonValidar.place(x=150, y=50)

ventana.mainloop()