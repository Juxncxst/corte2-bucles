x = int(input("Ingrese el número entero x: "))


min1 = int(input("Ingrese el límite inferior del intervalo 1: "))
max1 = int(input("Ingrese el límite superior del intervalo 1: "))


min2 = int(input("Ingrese el límite inferior del intervalo 2: "))
max2 = int(input("Ingrese el límite superior del intervalo 2: "))


min3 = int(input("Ingrese el límite inferior del intervalo 3: "))
max3 = int(input("Ingrese el límite superior del intervalo 3: "))

if x > min1 and x < max1:
    print(f"El número {x} está dentro del intervalo abierto ({min1}, {max1}).")
elif x > min2 and x < max2:
    print(f"El número {x} está dentro del intervalo abierto ({min2}, {max2}).")
elif x > min3 and x < max3:
    print(f"El número {x} está dentro del intervalo abierto ({min3}, {max3}).")
elif x <= min1 or x >= max1 and x <= min2 or x >= max2 and x <= min3 or x >= max3:
    print(f"El número {x} está FUERA de los tres intervalos.")
