# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

num = float(input("Ingrese un numero:  "))

parteDecimal = num % 1

print(f"La parte decimal del numero {num} es:  {parteDecimal}")