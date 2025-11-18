numero = int(input("Ingrese un número entero: "))

if numero > 0:
    temp = numero
    while temp > 0:
        cantidad_cifras += 1
        temp //= 10
    temp = numero
    suma = 0
    while temp > 0:
        digito = temp % 10
        suma += digito ** cantidad_cifras
        temp //= 10
    if suma == numero:
        print(numero, "ES un número de Armstrong.")
    else:
        print(numero, "NO es un número de Armstrong.")
else:
    print("El número no es positivo.")
