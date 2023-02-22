from Personaje import * #* = importa toda la clase.

#Creamos una instancia de la clase Personaje
Heroe = Personaje()

#Usamos los atributos 
print("El personaje se llama "+Heroe.nombre)
print("Pertenece a la especie "+Heroe.especie)
print("Tiene una altura de  "+str(Heroe.altura))

#Usar los métodos
Heroe.Correr(True)
Heroe.LanzarGranadas()
Heroe.RecargarArma(37)