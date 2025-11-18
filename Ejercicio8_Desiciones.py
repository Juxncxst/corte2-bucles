nota=float(input("Ingrese su nota: "))
if nota <3.0:
    print ("Su nota  " , nota ," es insuficiente")
elif nota >3.0 and nota <=3.5 :
     print ("Su nota " , nota ," es aceptable")
elif nota >3.5 and nota <=4.0 :
     print ("Su nota " , nota ," es sobresaliente")
else:
     print ("Su nota " , nota ," es Excelente")