from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import * #hacerlo antes de la instancia

#Instancia - puente entre los 2 archivos
controlador = ControladorBD()

#Metodo que usa el obj controlador para insertar
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())

ventana = Tk()
ventana.title('CRUD de usuarios.')
ventana.geometry('500x300')

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')  

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)

#Pestaña 1: formulario de registro
titulo = Label(pestaña1, text='Registro usuarios', fg='blue', font=('Modern', 18)).pack()
varNom = tk.StringVar()
lblNom = Label(pestaña1, text='Nombre: ').pack()
txtNom = Entry(pestaña1, textvariable=varNom).pack()

varCor = tk.StringVar()
lblCor = Label(pestaña1, text='Correo: ').pack()
txtCor = Entry(pestaña1, textvariable=varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestaña1, text='Contraseña: ').pack()
txtCon = Entry(pestaña1, textvariable=varCon).pack()

btnGuardar = Button(pestaña1, text='Guardar usuarios', command=ejecutaInsert).pack()

panel.add(pestaña1, text='Formulario usuario')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuario')
panel.add(pestaña4, text='Actualizar usuario')

ventana.mainloop()