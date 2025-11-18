valor= float (input("Ingrese el valor del articulo: "))
tipo=int(input("Ingrese el tipo de articulo: "))
V_Final= 0
if tipo ==1 :
    V_Final= valor - (valor* 12.5/100)
elif tipo == 2:
    V_Final= valor - (valor* 8.3/100)
elif tipo == 3:
    V_Final= valor - (valor* 3.2/100)
else:
    V_Final=valor

print(f"El valor final del articulo es: {V_Final}")