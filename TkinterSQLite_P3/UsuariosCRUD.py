from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import * #hacerlo antes de la instancia

#Instancia - puente entre los 2 archivos
controlador = ControladorBD()

#Metodo que usa el obj controlador para insertar
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())
#Metodo que usa el obj controlador para buscar
def ejecutaSelectU():
    rsUsu = controlador.consultarUsuario(varBus.get())
    #Iteramos el contenido de la consulta y lo guardamos en 'cadena'
    for usu in rsUsu:
        cadena = str(usu[0])+' '+usu[1]+' '+usu[2]+' '+str(usu[3])
    if(rsUsu):
        print(cadena)
    else:
        print('Usuario no existe en la BD')

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

#Pestaña 2:  buscar usuario
titulo2 = Label(pestaña2, text = 'Buscar usuario', fg='green', font=('Modern', 18)).pack()
varBus = tk.StringVar()
lblid = Label(pestaña2, text='Identificador de usuario: ').pack()
txtid = Entry(pestaña2, textvariable=varBus).pack() #caja de texto

subBus = Label(pestaña2, text='Registrado: ', fg='Blue', font=('Modern', 15)).pack()
textBus = tk.Text(pestaña2,  height=5, width=52).pack()

btnBusqueda = Button(pestaña2, varBus, text='Buscar', command=ejecutaSelectU).pack()

panel.add(pestaña1, text='Formulario usuario')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuario')
panel.add(pestaña4, text='Actualizar usuario')

ventana.mainloop()