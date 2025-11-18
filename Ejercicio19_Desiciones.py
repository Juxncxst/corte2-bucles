valor= float (input("Ingrese el valor del articulo: "))
tipo=(input("Ingrese el tipo de articulo: ").upper)
V_Final= 0
if tipo =="ELECTRODOMESTICO" :
    V_Final= valor - (valor* 3.7/100)
elif tipo == "ELEMENTO DE COCINA":
    V_Final= valor - (valor* 4.2/100)
elif tipo == "VIDEOJUEGO":
    V_Final= valor - (valor* 7.8/100)
else:
    V_Final=valor

print(f"El valor final del articulo es: {V_Final}")