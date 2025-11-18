n = int(input("Ingrese un número mayor que 1: "))
es_primo = True

for i in range(2, int(n**0.5) + 1): #se verifica hasta la raiz cuadrada de n**0.5
    if n % i == 0:
        es_primo = False
        break

if es_primo:
    print("El número es primo.")
else:
    print("El número NO es primo.")
