def grados(gradosf):
    gradosc=(gradosf-32)  *5/9
    return gradosc

gradosfarenheit=int(input("Ingrese grados F: "))

gradoscelcius=grados(gradosfarenheit)
print(gradosfarenheit, "grados Fahrenheit son", gradoscelcius, "grados Celsius.")