class Datos:
    from tkinter import Tk, Button, Frame, messagebox, simpledialog, Label, Entry
    def __init__(self, correo, contraseña):
        self.__correo = correo
        self.__contraseña = contraseña

    def getCorreo(self):
        return self.__correo
    def setCorreo(self, correo):
        self.__correo = correo

    def getContraseña(self):
        return self.__contraseña
    def setContraseña(self, contraseña):
        self.__contraseña = contraseña