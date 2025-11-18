n = int(input("¿Cuántos estudiantes participan en la encuesta? "))

votos_android = 0
votos_ios = 0

for i in range(n):
    print(f"\n--- Estudiante {i+1} ---")
    codigo = input("Ingrese el código del estudiante: ")
    voto = input("Ingrese su elección (Android / iOS): ").strip().lower()

    if voto == "android":
        votos_android += 1
    elif voto == "ios":
        votos_ios += 1
    else:
        print("Opción no válida. El voto NO será tenido en cuenta.")

print("\nRESULTADOS")
print("Votos por Android:", votos_android)
print("Votos por iOS:", votos_ios)

if votos_android > votos_ios:
    print("La plataforma elegida es: ANDROID")
elif votos_ios > votos_android:
    print("La plataforma elegida es: iOS")
else:
    print("Hay un EMPATE. Debe usarse otro mecanismo de elección.")
