from tkinter import *
from tkinter import ttk
import tkinter as tk
from archivo2 import *

controlador = ConstructorBD()

def ejecutaInsert():
    controlador.InsertarRegistro(varTrans.get(), varAduana.get())

ventana = Tk()
ventana.title('Exportaciones')
ventana.geometry('400x200')

panel = ttk.Notebook(ventana)
panel.pack(expand='yes')

pestaña1 = ttk.Frame(panel)
titulo1 = Label(pestaña1, text='Insertar registros', font=(15)).pack()
varTrans = tk.StringVar()
lblTrans = Label(pestaña1, text='Medio de transporte:').pack()
txtTrans = Entry(pestaña1, textvariable=varTrans).pack()

varAduana = tk.StringVar()
lblAduana = Label(pestaña1, text='Aduana:').pack()
txtAduana = Entry(pestaña1, textvariable=varAduana).pack()

btnInsertar = Button(pestaña1, text='Insertar', command=ejecutaInsert).pack()

panel.add(pestaña1, text='Insertar registro')

ventana.mainloop()