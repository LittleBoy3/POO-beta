def es_palindromo(cadena):

    cadena_sin_espacios = cadena.replace(" ", "")
 
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

cadena_ingresada = input("Ingrese una cadena de texto: ")

if es_palindromo(cadena_ingresada):
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")