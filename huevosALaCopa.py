# Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando la temperatura sobrepasa un punto crítico. A medida que la temperatura aumenta, las reacciones se aceleran. En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema lo hacen para temperaturas sobre 70°C. Para hacer un huevo a la copa, la clara debe haber sido calentada lo suficiente para coagularse a más de 63°C, pero la yema no debe sobrepasar los 70°C para evitar obtener un huevo duro.
# Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.


import math 

m1 = 47
m2 = 67
dens = 1.038

c = 3.7
k = 5.4e-3
tw = 100

tempO = float(input("Ingrese la temperatura original del huevo en grados celsius:  "))

m = m1 

ty = 70
t = (m**(2/3) * c * dens**(1/3)) / (k * math.pi**(4*3.1416/3)**(2/3)) * math.log(0.76 * (tempO - tw))

print(f"El tiempo necesario para alcanzar la temperatura máxima ({ty}°c) y preparar el huevo a la copa es de {t} segundos.")