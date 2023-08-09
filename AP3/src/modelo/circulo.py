import math

class Circulo:
    def __init___(self):
        self.radio=0
        self.centro=0
        self.coordenada_x=0
        self.coordenada_y=0

    def area(self):
        a= math.pi*self.radio**2
    def perimetro(self):
        diametro=self.radio*2
        perimetro=math.pi*diametro
    def calcular_distancia(self, punto):
        distancia= math.sqrt((self.coordenada_x-self.coordenada_y)**2+(punto.coordenada_x-punto.coordenada_y)**2)