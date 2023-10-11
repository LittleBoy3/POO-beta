from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    def __str__(self):
        return f"El libro con título {self.libro.titulo} y ISBN {self.libro.isbn} ya existe en el catálogo"

