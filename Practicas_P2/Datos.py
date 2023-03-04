from tkinter import Tk, Button, Frame, messagebox, simpledialog, Label, Entry
class Datos:

    def __init__(self, correo, contraseña, corr, cont):
        self.correo = correo
        self.__contraseña = contraseña
        self.__corr = corr
        self.__cont = cont

    def Validar(self):
        if(self.correo.get() == self.__corr and self.__contraseña.get() == self.__cont):
            messagebox.showinfo('Bienvenido','El inicio de sesión ha sido exitoso.')
        else:
            messagebox.showerror('Error','Datos incorrectos, favor de verificar los datos.')

    