from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro import Libro

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro: Libro, cantidad_a_comprar, existencias):
        super().__init__(libro)
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return f"El libro con título {self.libro.titulo} y ISBN {self.libro.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"