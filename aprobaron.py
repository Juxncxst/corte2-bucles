cantidad = int(input("¿Cuántos estudiantes tiene el grupo? "))

aprobados = 0
reprobados = 0
suma_notas = 0

for i in range(cantidad):
    print(f"\n--- Estudiante {i+1} ---")
    codigo = input("Ingrese el código del estudiante: ")
    nota = float(input("Ingrese la nota definitiva: "))
    
    suma_notas += nota
    
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

promedio = suma_notas / cantidad

print("\nRESULTADOS:")
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio general del grupo:", round(promedio, 2))
