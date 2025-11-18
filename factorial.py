n = int(input("Ingrese un número entero: "))
if n < 0:
    print("El número no tiene factorial.")
else:
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    print("El factorial de", n, "es:", factorial)
