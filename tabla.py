cantidad = int(input("Ingrese la cantidad de números: "))

while cantidad < 0:
    print("No se permiten valores negativos.")
    cantidad = int(input("Ingrese la cantidad de números: "))

for numero in range(1, cantidad + 1):
    print(numero, "\t", numero * numero, "\t", numero * numero * numero)
4
