from tkinter import Tk, Button, Frame

#1. Generar una ventana
ventana = Tk()
ventana.title('Ejemplo de 3 framnes - Practica 11')
ventana.geometry('600x400')
#2. Crear secciones (frames)
seccion1 = Frame(ventana, bg='blue')
seccion1.pack(expand = True, fill='both')

seccion2 = Frame(ventana, bg='pink')
seccion2.pack(expand = True, fill='both')

seccion3 = Frame(ventana, bg='yellow')
seccion3.pack(expand = True, fill='both')

#3.  Agregamos botones.
botonAzul = Button(seccion1, text = 'Soy el boton azul', fg = "Blue")
botonAzul.place(x = 60, y = 60, width = 100, height = 30)

botonNegro = Button(seccion2, text = 'Soy el boton negro', fg = "black")
botonNegro.grid(row = 0, column = 0)

botonAmarillo = Button(seccion2, text = 'Soy el boton amarillo', bg = "yellow")
botonAmarillo.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text = 'Soy el boton morado', fg = "purple")
botonVerde.pack()

ventana.mainloop() #Método para que se pueda ejecutar la ventana