a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = (b ** 2) - (4 * a * c)

if a == 0:
    print("No es una ecuación cuadrática porque a = 0.")
elif discriminante < 0:
    print("La ecuación NO tiene solución real (discriminante < 0).")
elif discriminante >= 0:
    print("La ecuación tiene solución real (discriminante >= 0).")