# Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo. El promedio del ramo se calcula con la siguiente formula. Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final. Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60. Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final. Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

cert1 = float(input("Ingrese nota certamen 1:  "))
cert2 = float(input("Ingrese nota certamen 2:  "))
lab = float(input("Ingrese nota laboratorio:  "))

prom = (cert1 + cert2) / 2
op = (prom * 0.7) + (lab * 0.3)

print(f"Para aprobar con nota 60, debe obtener una nota de {op}")

