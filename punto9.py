n = int(input("Ingrese un número: "))
for i in range(n, -1, -1):
    if i % 7 == 0 and i != 0:#Se agrega and i != 0 para no marcar el 0 como múltiplo
        print(i, "múltiplo de 7")
    else:
        print(i)
