lista_original = [1, 2, 3, 4, 5,6,7,8,9,10]
lista_invertida = []

for i in range(len(lista_original) - 1, -1, -1):
    lista_invertida.append(lista_original[i])

print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)