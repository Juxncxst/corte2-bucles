n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
n4 = float(input("Ingrese el cuarto número: "))

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    mayor = n1
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    mayor = n2
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    mayor = n3
else:
    mayor = n4

print(f"El número mayor es: {mayor}")
