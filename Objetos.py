from Personaje import * #* = importa toda la clase.
#2. Solicitamos los parametros.
print('¡Solicitud de datos para el heroe!')
especieH = input('Escribe la especie del heroe: ')
nombreH = input('Escribe el nombre del heroe: ')
alturaH = float(input('Escribe la altura del heroe: '))
recargaH = int(input('Escriba cuantas balas desea que tenga el heroe: '))
print('')
print('¡Solicitud de datos para el villano!')
especieV = input('Escribe la especia del villano: ')
nombreV = input('Escribe el nombre del villano: ')
alturaV = float(input('Escribe la altura del villano: '))
recargaV = int(input('Escriba cuantas balas desea que tenga el villano: '))

#3. Creamos los objetos
Heroe = Personaje(especieH, nombreH, alturaH)
Villano = Personaje(especieV, nombreV, alturaV)


#4. Usamos los atributos del heroe y villano
print('')
print('¡HEROE!')
print("El personaje se llama "+Heroe.getNombre())
print("Pertenece a la especie "+Heroe.getEspecie())
print("Tiene una altura de  "+str(Heroe.getAltura()))
Heroe.Correr(True)
Heroe.LanzarGranadas()
Heroe.RecargarArma(recargaH)

print('')
print('¡VILLANO!')
print("El personaje se llama "+Villano.getNombre())
print("Pertenece a la especie "+Villano.getEspecie())
print("Tiene una altura de  "+str(Villano.getAltura()))
Villano.Correr(True)
Villano.LanzarGranadas()
Villano.RecargarArma(recargaV)

