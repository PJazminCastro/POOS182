from tkinter import Entry, ttk, Tk, Button, Frame, Label, messagebox, simpledialog;
from DatosP14 import *;
import tkinter as tk;

ventana = Tk()
ventana.title('Caja popular - Practica 14')
ventana.geometry('250x400')

seccion = Frame(ventana, bg='#EBEBEB')
seccion.pack(expand = True, fill='both')

SolicitudNoCuent = Label(seccion, text='Ingrese el No. de cuenta: ')
SolicitudNoCuent.place(x=50, y=50)
VarNoCuen = tk.StringVar
NoCuenta = tk.Entry(seccion, textvariable=VarNoCuen)
NoCuenta.place(x=50, y=70)

SolicitudTitular = Label(seccion, text='Ingrese el nombre del titular: ')
SolicitudTitular.place(x=50, y=100)
VarTitular = tk.StringVar
Titular = tk.Entry(seccion, textvariable=VarNoCuen)
Titular.place(x=50, y=120)

SolicitudEdad = Label(seccion, text='Ingrese la edad del titular: ')
SolicitudEdad.place(x=50, y=150)
VarEdad = tk.StringVar
Edad = tk.Entry(seccion, textvariable=VarNoCuen)
Edad.place(x=50, y=170)

Saldo = 0
Deposito = 0
Retiro = 0

consulta = DatosP14(NoCuenta, Titular, Edad, Saldo, Deposito, Retiro)

botonConsultaS = Button(seccion, text='Consulta de saldo', command=consulta.ConsultaSaldo)
botonConsultaS.place(x=50, y=200)

botonDeposito = Button(seccion, text='Depositar a cuenta propia', command=consulta.DepositoCP)
botonDeposito.place(x=50, y=235)

botonRetiro = Button(seccion, text='Retiro a cuenta propia', command=consulta.Retiro)
botonRetiro.place(x=50, y=270)

botonDepositoOtro = Button(seccion, text='Depositar a cuenta externa', command=consulta.DepositoCP)
botonDepositoOtro.place(x=50, y=305)

ventana.mainloop()