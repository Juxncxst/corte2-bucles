while True:
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "3":
        print("Saliendo del programa...")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print("Resultado:", num1 + num2)
    elif opcion == "2":
        print("Resultado:", num1 - num2)
    else:
        print("Opción no válida.")
