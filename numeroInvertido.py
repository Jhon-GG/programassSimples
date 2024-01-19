# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

num = int(input("Ingrese un número de tres dígitos: "))

if 100 <= num <= 999:
    num_inverso = int(str(num)[::-1])
    print("El número con los dígitos en orden inverso es:", num_inverso)
else:
    print("Por favor, ingrese un número de tres dígitos.")

