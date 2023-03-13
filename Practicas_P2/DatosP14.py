from tkinter import Tk, Button, Frame, messagebox, simpledialog;
class DatosP14:
    def __init__(self, NoCuenta, Titular, Edad, Saldo, Deposito, Retiro):
        self.__NoCuenta = NoCuenta
        self.__Titular = Titular
        self.__Edad = Edad
        self.__Saldo = Saldo
        self.__Deposito = Deposito
        self.__Retiro = Retiro
        
    def ConsultaSaldo(self):
        NoCuenta1 = "121037801"
        Titular1 = 'Paola Castro'
        Edad1 = "19"
        Saldo1 = 1300
        NoCuenta2 = "121037808"
        Titular2 = 'Said Cuevas'
        Edad2 = "23"
        Saldo2 = 2300

        print(self.__NoCuenta.get())

        if(self.__NoCuenta.get() == NoCuenta1):
            if(self.__Titular.get() == Titular1):
                self.__Saldo = Saldo1
                messagebox.showinfo('Consulta saldo', 'Su saldo actual es: $'+str(self.__Saldo))
            else:
                messagebox.showerror('Error', 'Los datos ingresados son incorrectos')
        else: 
            if(self.__NoCuenta.get() == NoCuenta2):
                if(self.__Titular.get() == Titular2):
                    self.__Saldo = Saldo2
                    messagebox.showinfo('Consulta saldo', 'Su saldo actual es: $'+str(self.__Saldo))
                else:
                    messagebox.showerror('Error', 'Los datos ingresados son incorrectos')
            else:
                messagebox.showerror('Error', 'La cuenta ingresada no existe')

    def DepositoCP(self):
        NoCuenta1 = "121037801"
        Titular1 = 'Paola Castro'
        Edad1 = "19"
        Saldo1 = 1300
        NoCuenta2 = "121037808"
        Titular2 = 'Said Cuevas'
        Edad2 = "23"
        Saldo2 = 2300
        if(self.__NoCuenta.get() == NoCuenta1):
            if(self.__Titular.get() == Titular1):
                self.__Deposito = simpledialog.askfloat(title="Cantidad", prompt="¿Cuánto desea depositar?:")
                self.__Saldo = Saldo1 + self.__Deposito
                messagebox.showinfo('Deposito', 'Su saldo actual es: $'+str(self.__Saldo))
            else:
                messagebox.showerror('Error', 'Los datos ingresados son incorrectos')
        else: 
            if(self.__NoCuenta.get() == NoCuenta2):
                if(self.__Titular.get() == Titular2):
                    self.__Deposito = simpledialog.askfloat(title="Cantidad", prompt="¿Cuánto desea depositar?:")
                    self.__Saldo = Saldo1 + self.__Deposito
                    self.__Saldo = Saldo2
                    messagebox.showinfo('Consulta saldo', 'Su saldo actual es: $'+str(self.__Saldo))
                else:
                    messagebox.showerror('Error', 'Los datos ingresados son incorrectos')
            else:
                messagebox.showerror('Error', 'La cuenta ingresada no existe')

    def Retiro(self):
        NoCuenta1 = "121037801"
        Titular1 = 'Paola Castro'
        Edad1 = "19"
        Saldo1 = 1300
        NoCuenta2 = "121037808"
        Titular2 = 'Said Cuevas'
        Edad2 = "23"
        Saldo2 = 2300
        if(self.__NoCuenta.get() == NoCuenta1):
            if(self.__Titular.get() == Titular1):
                self.__Retiro = simpledialog.askfloat(title="Cantidad", prompt="¿Cuánto desea retirar?:")
                self.__Saldo = Saldo1 - self.__Retiro
                messagebox.showinfo('Deposito', 'Su saldo actual es: $'+str(self.__Saldo))
            else:
                messagebox.showerror('Error', 'Los datos ingresados son incorrectos')
        else: 
            if(self.__NoCuenta.get() == NoCuenta2):
                if(self.__Titular.get() == Titular2):
                    self.__Retiro = simpledialog.askfloat(title="Cantidad", prompt="¿Cuánto desea retirar?:")
                    self.__Saldo = Saldo1 - self.__Retiro
                    self.__Saldo = Saldo2
                    messagebox.showinfo('Consulta saldo', 'Su saldo actual es: $'+str(self.__Saldo))
                else:
                    messagebox.showerror('Error', 'Los datos ingresados son incorrectos')
            else:
                messagebox.showerror('Error', 'La cuenta ingresada no existe')