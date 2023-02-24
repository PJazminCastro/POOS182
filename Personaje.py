class Personaje:
    #1. Constructor
    def __init__(self, esp, nom, alt):
        self.__especie = esp #Se encapsularon con los 2 guiones
        self.__nombre = nom
        self.__altura = alt

    #Métodos
    def Correr(self, status):
        if(status): 
            print("El personaje "+self.__nombre+" esta corriendo.")
        else: print("El personaje "+self.__nombre+" se detuvo.")

    def LanzarGranadas(self):
        print("El personaje "+self.__nombre+" lanzo una granada.")

    def RecargarArma(self, municiones):
        cargador = 10
        cargador = cargador + municiones
        print("El arma recargada tiene "+str(cargador)+" balas.")

    #Se generan los getters y setters
    def getEspecie(self):
        return self.__especie
    def setEspecie(self, esp):
        self.__especie = esp

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nom):
        self.__nombre = nom
    
    def getAltura(self):
        return self.__altura
    def setAltura(self, alt):
        self.__altura = alt