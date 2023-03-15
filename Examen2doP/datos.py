from tkinter import Tk, Button, Frame, messagebox, simpledialog, Label, Entry
import secrets; import string; import tkinter as tk;
class Datos:
    def __init__(self, Nombre, ApellidoP, ApellidoM, AñoN, Carrera, Longitud):
        self.__Nombre = Nombre
        self.__ApellidoP = ApellidoP
        self.__ApellidoM = ApellidoM
        self.__AñoN = AñoN
        self.__Carrera = Carrera
        self.__Longitud = Longitud

    def Generar(self):
        digitos = string.digits
        
        pwd = ' '
        añoC = ('23')
        cadenaAño = self.__AñoN.get()
        cadenaNombre = self.__Nombre.get()
        cadenaApellidoP = self.__ApellidoP.get()
        cadenaApellidoM = self.__ApellidoM.get()
        cadenaCarrera = self.__Carrera.get()
        digitosAño = cadenaAño[2:4]
        digitosNombre = cadenaNombre[0]
        digitosApellidoP = cadenaApellidoP[0]
        digitosApellidoM = cadenaApellidoM[0]
        digitosCarrera = cadenaCarrera[:3]
        
        Alfabeto = añoC + digitosAño + digitos
        for i in range(self.__Longitud):
            pdw += ''.join(secrets.choice(Alfabeto))
            
        messagebox.showinfo('Matricula', añoC+digitosAño+digitosNombre+digitosApellidoP+digitosApellidoM+digitos+digitosCarrera)