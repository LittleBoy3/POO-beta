from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __str__(self):
        return f"El libro con título {self.libro.titulo} y ISBN {self.libro.isbn} está agotado"