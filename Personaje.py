class Personaje:

    #Atributos
    especie = "Humano"
    nombre = "MasterChief"
    altura = 2.70

    #Métodos
    def Correr(self, status):
        if(status): 
            print("El personaje "+self.nombre+" esta corriendo.")
        else: print("El personaje "+self.nombre+" se detuvo.")

    def LanzarGranadas(self):
        print("El personaje "+self.nombre+" lanzo una granada.")

    def RecargarArma(self, municiones):
        cargador = 10
        cargador = cargador + municiones
        print("El arma recargada tiene "+str(cargador)+" balas.")