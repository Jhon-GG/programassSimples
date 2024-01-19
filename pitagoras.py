# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.
cateto1 = float(input("Ingrese el valor del primer cateto:  "))
cateto2 = float(input("Ingrese el valor delsegundo cateto:  "))

hipotenusa = (cateto1**2 + cateto2**2)**0.5

print (f"La hipotenusa es:  {hipotenusa}")