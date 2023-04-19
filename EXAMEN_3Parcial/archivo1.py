from tkinter import *
from tkinter import ttk
import tkinter as tk
from archivo2 import *

controlador = ConstructorBD()

def ejecutaInsert():
    controlador.InsertarRegistro(varTrans.get(), varAduana.get())
def ejecutaBorrarR():
    controlador.eliminarRegistros(varID.get())

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

pestaña2 = ttk.Frame(panel)
titulo2 = Label(pestaña2, text='Eliminar registros', font=(15)).pack()
varID = tk.StringVar()
lblID = Label(pestaña2, text='ID de registro:').pack()
txtID = Entry(pestaña2, textvariable=varID).pack()

btnEliminar = Button(pestaña2, text='Eliminar', command=ejecutaBorrarR).pack()

panel.add(pestaña1, text='Insertar registro')
panel.add(pestaña2, text='Eliminar registro')


ventana.mainloop()