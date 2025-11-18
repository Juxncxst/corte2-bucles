n1 = float(input("Ingrese la nota del trabajo 1: "))
n2 = float(input("Ingrese la nota del trabajo 2: "))
n3 = float(input("Ingrese la nota del trabajo 3: "))
n4 = float(input("Ingrese la nota del trabajo 4: "))
n5 = float(input("Ingrese la nota del trabajo 5: "))

promedio = (n1 + n2 + n3 + n4 + n5) / 5

if promedio > 3.5:
    print(f"Nota definitiva: {promedio:.2f}. ¡Ganó el curso!")
elif promedio <= 3.5:
    print(f"Nota definitiva: {promedio:.2f}. Perdio el curso")
