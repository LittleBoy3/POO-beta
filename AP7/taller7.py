from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre

@dataclass
class Conjunto:
    contador = 0  # se define el contador de instancias de conjunto

    def __init__(self, nombre):
        self.nombre = nombre  # se inicializa el atributo nombre
        self.elementos = []   # se inicializala listade elementos
        self.__id = Conjunto.contador  # se inicializa el atributo privado __id
        Conjunto.contador += 1  # incrementa el contador de instancias

    @property
    def id(self):
        return self.__id  # define una propiedad de solo lectura id

    def contiene(self, elemento):
        return any(elemento == e for e in self.elementos)  # verifica si el elemento ya está en el conjunto

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):  # agrega el elemento si no está contenido en el conjunto
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")  # crea un nuevo conjunto
        for elemento in self.elementos + otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)  # agrega elementos al nuevo conjunto
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)  # define el operador de suma como unión de conjuntos

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [e for e in conjunto1.elementos if conjunto2.contiene(e)]  # encuentra elementos comunes
        nombre_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        return cls(nombre_resultante)  # crea un nuevo conjunto con la intersección

    def __str__(self):
        elementos_str = ", ".join(e.nombre for e in self.elementos)  # representación en cadena
        return f"Conjunto {self.nombre}: ({elementos_str})"

# Ejemplo de uso
elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

conjunto1 = Conjunto("Conjunto 1")  # crear una instancia de conjunto
conjunto1.agregar_elemento(elemento1)  # aagregar elementos al conjunto
conjunto1.agregar_elemento(elemento2)

conjunto2 = Conjunto("Conjunto 2")
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

print(conjunto1)
print(conjunto2)

conjunto3 = conjunto1 + conjunto2  # unir dos conjuntos con el operador +
print(conjunto3)

conjunto4 = Conjunto.intersectar(conjunto1, conjunto2)  #intersección de conjuntos
print(conjunto4)