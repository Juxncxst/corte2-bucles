nivel = float(input("Ingrese el nivel actual del tanque en litros: "))

if nivel < 250:
    print("La llave debe estar ABIERTA (el tanque está muy vacío).")
elif nivel > 450:
    print("La llave debe estar CERRADA (el tanque está lleno o se está desbordando).")
else:
    print("La llave debe estar CERRADA (el nivel está dentro del rango normal).")
