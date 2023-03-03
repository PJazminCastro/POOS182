from tkinter import Tk, Button, Frame, messagebox, simpledialog, Label, Entry
from SoluciónP12 import *;

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
correoP = Entry(seccionCorreo)
correoP.place(x=150, y=50)

solicitudContraseña = Label(seccionContraseña, text='Ingrese su contraseña: ')
solicitudContraseña.place(x=25, y=50)
contraseñaP = Entry(seccionContraseña, show='*')
contraseñaP.place(x=150, y=50)

correoI = ('121037801@upq.edu.mx')
contraseñaI = ('121037801upq')

Predeterminado = Datos(correoI, contraseñaI)
Usuario = Datos(correoP, contraseñaP)



def Validar():
    print(correoP.get())
    print(contraseñaP.get())
    if(correoP):
        if(contraseñaP.get() == contraseñaI):
            messagebox.showinfo('Bienvenido','El inicio de sesión ha sido exitoso.')
        else: 
            messagebox.showerror('Error', 'La contraseña es incorrecta')
    else:
        messagebox.showerror('Error','No se encontro una cuenta asociada al correo ingresado.')

botonValidar = Button(seccionBoton, text='Iniciar sesión', command=Validar)
botonValidar.place(x=150, y=50)

ventana.mainloop()