def media_aritmetica(lista):
    if not lista:
        return None

    suma = sum(lista)
    media = suma / len(lista)
    return media

lista_numeros = [1, 2, 3, 4]
resultado = media_aritmetica(lista_numeros)
print("La media aritmética de la lista es:", resultado)