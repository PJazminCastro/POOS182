from tkinter import *;
from DatosP13 import *;
import tkinter as tk


ventana = Tk()
ventana.title('Inicio de sesión - Practica 12')
ventana.geometry('300x400')

seccionLongitud = Frame(ventana, bg='#EBEBEB')
seccionLongitud.pack(expand = True, fill='both')

seccionMayusc = Frame(ventana, bg='#EBEBEB')
seccionMayusc.pack(expand = True, fill='both')

seccionCaractE = Frame(ventana, bg='#EBEBEB')
seccionCaractE.pack(expand = True, fill='both')

seccionBoton = Frame(ventana, bg='#EBEBEB')
seccionBoton.pack(expand = True, fill='both')

solicitudLong = Label(seccionLongitud, text='Ingrese la longitud deseada (minimo 8): ')
solicitudLong.place(x=50, y=50)
VarLong = tk.StringVar()
LongP = Entry(seccionLongitud, textvariable=VarLong)
LongP.place(x=150, y=50)

solicitudMayusc = Label(seccionMayusc, text='¿Desea que contenga mayusculas?: ')
solicitudMayusc.place(x=25, y=50)
MayuscP = Entry()
MayuscP.place(x=150, y=50)

solicitudCaracE = Label(seccionCaractE, text='¿Desea que contenga mayusculas?: ')
solicitudCaracE.place(x=25, y=50)
CaracP = Entry()
CaracP.place(x=150, y=50)

validacion = DatosP13(LongP, MayuscP, CaracP)

botonGenerar = Button(seccionBoton, text='Generar', command = validacion.Generar)
botonGenerar.place(x=150, y=50)

ventana.mainloop()