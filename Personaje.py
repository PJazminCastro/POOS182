class Personaje:
    #1. Constructor
    def __init__(self, esp, nom, alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt

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
