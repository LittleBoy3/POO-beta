def factorial(numero):
    if numero < 0:
        return None
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
numero = int(input("ingrese el numero para sacar el factorial: "))
resultado = factorial(numero)

if resultado is None:
    print("El factorial no está definido para números negativos.")
else:
    print("El factorial de", numero, "es:", resultado)