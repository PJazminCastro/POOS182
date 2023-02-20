class Personaje:

    #Atributos
    especie = "Humano"
    nombre = "MasterChief"
    altura = 2.70

    #Métodos
    def Correr(self, status):
        if(status): 
            print("El personaje "+self.nombre+" esta corriendo")
        else: print("El personaje "+self.nombre+" se detuvo")