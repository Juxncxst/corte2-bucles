num = int(input("Ingresa un número del 0 al 20: "))

if num < 0 or num > 20:
    print("Número fuera de rango.")
else:
    # Los números menores que 2 no son primos
    if num < 2:
        print(f"{num} no es un número primo.")
    else:
        es_primo = True
        # Revisamos divisores desde 2 hasta num
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f"{num} es un número primo.")
        else:
            print(f"{num} no es un número primo.")
