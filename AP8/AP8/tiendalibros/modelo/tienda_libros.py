from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError



class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            
            raise LibroExistenteError(isbn, self.catalogo[isbn].titulo)
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, isbn, cantidad):
        if isbn not in self.catalogo:
            raise Exception("El libro no existe en el catálogo")
        libro = self.catalogo[isbn]

        if libro.existencias == 0:
            
            raise LibroAgotadoError(isbn, libro.titulo)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(isbn, libro.titulo, cantidad, libro.existencias)

        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)