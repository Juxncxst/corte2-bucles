n = int(input("Ingrese un número entero: "))
invertido = 0

while n != 0:
    digito = n % 10 # saca el ultimo digito de n
    invertido = invertido * 10 + digito # aqui multiplicamos el num ivertido por 10 y se le suma el digito
    n //= 10#esto elimina el ultimo digito del num en cada iteracion y cuando esto es 0 se acaba el ciclo

print("Número invertido:", invertido)
