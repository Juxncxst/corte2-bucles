clave_correcta = "python123"
intentos = 0

while intentos < 3:
    clave = input("Ingrese la clave: ")
    if clave == clave_correcta:
        print("Acceso permitido")
        break
    else:
        intentos += 1
        print("Clave incorrecta. Intento", intentos, "de 3")

if intentos == 3:
    print("Acceso denegado. Demasiados intentos.")
