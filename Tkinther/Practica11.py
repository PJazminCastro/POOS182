from tkinter import Tk, Button, Frame, messagebox, simpledialog

#5. Agregar función de mensaje
def MostrarMensaje():
    messagebox.showinfo('Información','Te informo que todo fallo con exito.')
    messagebox.showerror('Error', '¡Perdon te falle!')
    print(messagebox.askokcancel('Pregunta', '¿Seguro que quieres guardar algo?'))
    print(messagebox.askyesnocancel('Pregunta', '¿Seguro que quieres guardar algo?'))
    #Tareaaaa
    simpledialog.askstring(title="Test", prompt="¿Cuál es tu nombre?:")

#6. Función agregar boton
def AgregarBoton():
    botonVerde.config(text='+', bg = 'Green', fg = 'White')
    botonNuevo = Button(seccion3, text = 'Boton nuevo.')
    botonNuevo.pack()

#1. Generar una ventana
ventana = Tk()
ventana.title('Ejemplo de 3 framnes - Practica 11')
ventana.geometry('600x400')
#2. Crear secciones (frames)
seccion1 = Frame(ventana, bg='#a5b2ff')
seccion1.pack(expand = True, fill='both')

seccion2 = Frame(ventana, bg='#ddbaba')
seccion2.pack(expand = True, fill='both')

seccion3 = Frame(ventana, bg='yellow')
seccion3.pack(expand = True, fill='both')

#3.  Agregamos botones.
botonAzul = Button(seccion1, text = 'Soy el boton azul', fg = "Blue", command = MostrarMensaje)
botonAzul.place(x = 60, y = 60, width = 100, height = 30)

botonNegro = Button(seccion2, text = 'Soy el boton negro', fg = "black")
botonNegro.grid(row = 0, column = 0)

botonAmarillo = Button(seccion2, text = 'Soy el boton amarillo', bg = "#dbdb04")
botonAmarillo.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text = 'Soy el boton verde', fg = "green", command =  AgregarBoton)
botonVerde.pack()

ventana.mainloop() #Método para que se pueda ejecutar la ventana