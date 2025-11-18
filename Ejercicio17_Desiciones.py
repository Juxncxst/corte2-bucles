x = int(input("Ingrese el número entero x: "))
minimo = int(input("Ingrese el valor mínimo del intervalo: "))
maximo = int(input("Ingrese el valor máximo del intervalo: "))

if x >= minimo and x <= maximo:
    print(f"El número {x} está DENTRO del intervalo [{minimo}, {maximo}].")
elif x < minimo or x > maximo:
    print(f"El número {x} está FUERA del intervalo [{minimo}, {maximo}].")