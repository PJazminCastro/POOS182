from tkinter import Tk, Button, Frame, messagebox, simpledialog, Label, Entry
import secrets; import string; import tkinter as tk;
class DatosP13:

    def __init__(self, longitud, mayusc, caractE):
        self.__longitud = tk.StringVar()
        self.__mayuc = mayusc
        self.__caractE = caractE

    def Generar(self):
        #validar que longitud sea >=8
        self.__longitud = tk.StringVar()
        longi= int(self.__longitud.get())
        if(longi >= 8):
            mayusc = messagebox.askyesno('Mayusculas', '¿Desea que su contraseña cuente con mayusculas?')
            print(mayusc)
            caractE = messagebox.askyesno('Caracter especial', '¿Desea que contenga caracteres especiales (@, _, -, *, +)?')
            print(caractE)
            #Validar si quiere mayuculas
            if(mayusc == True):
                Mayuscula = string.ascii_letters
                alfabeto = Mayuscula
                #validar si quiere caracteres
                if(caractE == True):
                    Caracter = string.punctuation
                    alfabeto = Mayuscula + Caracter
            else:
                if(caractE == True):
                    Caracter = string.punctuation
                    alfabeto = Caracter
                else:
                    messagebox.showerror('Error', 'Debe contener minimo alguna mayuscula o caracter especial')  
        else:
            messagebox.showerror('Error','La longitud minima es de 8 caracteres.')