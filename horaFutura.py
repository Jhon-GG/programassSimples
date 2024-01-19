# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

hora = float(input("Ingrese la hora actual:  "))
cantidad = float(input("Ingrese la cantidad de horas en las que desea saber la hora:  "))

horaNueva = (hora + cantidad) % 24

print (f"La hora después de {cantidad} horas, será:  {horaNueva}")