n = int(input("Ingrese el número inicial N: "))
m = int(input("Ingrese el número final M: "))
encontrado = False

for i in range(n, m + 1):
    if i % 9 == 0:
        print("El primer múltiplo de 9 es:", i)
        encontrado = True
        break

if not encontrado:
    print("No hay múltiplos de 9 en ese rango.")
