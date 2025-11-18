tabla = int(input("¿Qué tabla desea repasar? (1 a 20): "))

while tabla < 1 or tabla > 20:
    print("Tabla inválida. Debe ser entre 1 y 20.")
    tabla = int(input("Ingrese nuevamente la tabla: "))

aciertos = 0

print(f"\nRepasemos la tabla del {tabla}:\n")

for i in range(1, 11):
    respuesta = int(input(f"{tabla} x {i} = "))

    if respuesta == tabla * i:
        print("¡Correcto! Muy bien.")
        aciertos += 1
    else:
        print(f"Incorrecto. La respuesta correcta es {tabla * i}.")

print("\nRESULTADOS")
print("Aciertos:", aciertos)

if aciertos <= 5:
    valoracion = "Insuficiente"
elif aciertos <= 7:
    valoracion = "Aceptable"
elif aciertos <= 9:
    valoracion = "Sobresaliente"
else:
    valoracion = "Excelente"

print("Valoración:", valoracion)
