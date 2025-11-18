import time

dias = 0
horas = 0
minutos = 0
segundos = 0

while True:
 
    print(f"Día {dias} - {horas:02d}:{minutos:02d}:{segundos:02d}")

    time.sleep(1)  
    segundos += 1 
    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        horas += 1

    if horas == 24:
        horas = 0
        dias += 1
