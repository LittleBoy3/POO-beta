lista_numeros = [12, 3, 44, 67, 8, 99, 1]

maximo = minimo = lista_numeros[0]
for numero in lista_numeros:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)