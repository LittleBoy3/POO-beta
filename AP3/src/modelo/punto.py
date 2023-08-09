from math import sqrt

class Punto:
    def __init___(self):
        self.coordenada_x=0
        self.coordenada_y=0
        
    def mostrar_coordenadas(self):
        print("las coordenadas son: ", self.coordenada_x, self.coordenada_y)
    def mover_coordenadas(self, coordenadas_x, coordenadas_y):
        self.coordenada_x=coordenadas_x
        self.coordenada_y=coordenadas_y
    def calcular_distancia(self, punto2):
        distancia= sqrt((self.coordenada_x-self.coordenada_y)**2+(punto2.coordenada_x-punto2.coordenada_y)**2)
        return distancia