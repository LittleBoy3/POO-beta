import random
tamaño_lista=10
desde=1
hasta=100
lista=[]
for i in range(tamaño_lista):
 lista.append(random.randint(desde,hasta))
print(lista)