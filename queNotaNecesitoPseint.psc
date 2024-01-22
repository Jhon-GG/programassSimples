Algoritmo queNotaNecesito
	Definir cert1, cert2, lab, prom, op Como Real
	Escribir "Ingrese nota certamen 1:  "
	Leer cert1
	Escribir "Ingrese nota certamen 2:  "
	Leer cert2
	Escribir "Ingrese nota laboratorio:  "
	Leer lab
	
	prom = (cert1 + cert2) / 2
	op = (prom * 0.7) + (lab * 0.3)
	
	Imprimir "Para aprobar con nota 60, debe obtener una nota  de:  ", op
FinAlgoritmo
