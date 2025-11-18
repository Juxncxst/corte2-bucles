art=float(input("Ingrese el valor del articulo: "))
val=0
if art>150.000:
    val= art - (art* 5/100)
else:
    val=art
 
print(f"El valor final del articulo es: {val}")