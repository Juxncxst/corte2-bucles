pares = 0
impares = 0

while True:
    n = int(input("Ingrese un número (0 para salir): "))
    if n == 0:
        break
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
