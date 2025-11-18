

sexo = input("Ingrese el sexo del aspirante (M para mujer / H para hombre): ").upper()
edad = int(input("Ingrese la edad del aspirante: "))
estatura = float(input("Ingrese la estatura en metros: "))
estado_civil = input("Ingrese el estado civil (soltero/casado): ").lower()


if sexo == "M" and estatura > 1.60 and 20 <= edad <= 25 and estado_civil == "soltero":
    print("La aspirante es APTA para ingresar al ejército.")
elif sexo == "H" and estatura > 1.65 and 18 <= edad <= 24 and estado_civil == "soltero":
    print("El aspirante es APTO para ingresar al ejército.")
else:
    print("El aspirante NO es apto para ingresar al ejército.")
