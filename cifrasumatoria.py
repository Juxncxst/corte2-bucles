numero = int(input("Ingrese un número entero: "))

if numero > 0:
    temp = numero
    cantidad_cifras = 0
    suma_cifras = 0

    while temp > 0:
        digito = temp % 10       
        suma_cifras += digito    
        cantidad_cifras += 1     
        temp //= 10              

    print("El número es positivo.")
    print("Cantidad de cifras:", cantidad_cifras)
    print("Suma de las cifras:", suma_cifras)

else:
    print("El número no es positivo.")
