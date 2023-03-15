from tkinter import Entry, ttk, Tk, Button, Frame, Label, messagebox, simpledialog;
from datos import *;
import tkinter as tk;

ventana = Tk()
ventana.title('Caja popular - Practica 14')
ventana.geometry('250x400')

seccion = Frame(ventana, bg='#EBEBEB')
seccion.pack(expand = True, fill='both')

SolicitudNombre = Label(seccion, text='Ingrese su/s nombre/s: ')
SolicitudNombre.place(x=50, y=50)
VarNombre = tk.StringVar
Nombre = tk.Entry(seccion, textvariable=VarNombre)
Nombre.place(x=50, y=70)

SolicitudApellidoP = Label(seccion, text='Ingrese su apellido paterno: ')
SolicitudApellidoP.place(x=50, y=100)
VarApellidoP = tk.StringVar
ApellidoP = tk.Entry(seccion, textvariable=VarApellidoP)
ApellidoP.place(x=50, y=120)

SolicitudApellidoM = Label(seccion, text='Ingrese su apellido materno: ')
SolicitudApellidoM.place(x=50, y=150)
VarApellidoM = tk.StringVar
ApellidoM = tk.Entry(seccion, textvariable=VarApellidoM)
ApellidoM.place(x=50, y=170)

SolicitudAño = Label(seccion, text='Ingrese su año de nacimiento: ')
SolicitudAño.place(x=50, y=200)
VarAño = tk.StringVar
Año = tk.Entry(seccion, textvariable=VarAño)
Año.place(x=50, y=220)

SolicitudCarrera = Label(seccion, text='Ingrese su carrera: ')
SolicitudCarrera.place(x=50, y=250)
VarCarrera = tk.StringVar
Carrera = tk.Entry(seccion, textvariable=VarCarrera)
Carrera.place(x=50, y=270)

Longitud = 13

generar = Datos(Nombre, ApellidoP, ApellidoM, Año, Carrera, Longitud)

botonGenerar = Button(seccion, text='Generar matricula', command=generar.Generar)
botonGenerar.place(x=50, y=300)

ventana.mainloop()