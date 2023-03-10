from tkinter import Tk, Button, Frame, messagebox, simpledialog, Label, Entry
import secrets; import string; import tkinter as tk;
class DatosP13:

    def __init__(self, longitud, mayusc, caractE):
        self.__longitud = 12
        self.__mayuc = mayusc
        self.__caractE = caractE

    def Generar(self):
        #validar que longitud sea >=8
            print(self.__longitud)
            print(self.__mayuc)
            print(self.__caractE)
            #Validar si quiere mayuculas
            if(self.__mayuc.get() == 'Si'):
                Mayuscula = string.ascii_letters
                alfabeto = Mayuscula
                #validar si quiere caracteres
                if(self.__caractE.get() == 'Si'):
                    Caracter = string.punctuation
                    alfabeto = Mayuscula + Caracter
                    pdw = ''
                    for i in range(self.__longitud):
                        pdw += ''.join(secrets.choice(alfabeto))
                    messagebox.showinfo('Contraseña',pdw)
                else: 
                    alfabeto = Mayuscula
                    pdw = ''
                    for i in range(self.__longitud):
                        pdw += ''.join(secrets.choice(alfabeto))
                    messagebox.showinfo('Contraseña',pdw)
            else:
                if(self.__caractE.get() == 'Si'):
                    Caracter = string.punctuation
                    alfabeto = Caracter
                    pdw = ''
                    for i in range(self.__longitud):
                        pdw += ''.join(secrets.choice(alfabeto))
                    messagebox.showinfo('Contraseña', pdw)
                else:
                    messagebox.showerror('Error', 'Debe contener minimo alguna mayuscula o caracter especial')  
        