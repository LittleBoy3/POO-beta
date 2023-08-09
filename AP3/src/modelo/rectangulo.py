class Rectangulo:
    def __init___(self):
        self.esquina1=0
        self.esquina2=0
        self.long1=0
        self.long2=0
        self.long3=0
        self.long4=0
        self.anch=0

    def perimetro(self):
        p=2(self.long1) + 2(self.anch)
    def area(self):
        a=self.long1*self.anch
    def elrectanculo_es_cuadrado(self):
     if self.long1==self.long2==self.long3==self.long4:
        print("El rectangulo es un cuadrado")


