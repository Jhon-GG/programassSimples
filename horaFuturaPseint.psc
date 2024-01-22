Algoritmo horaFutura
	Definir hora, cant, horaNueva Como Real
	Escribir "Ingrese la hora actual:  "
	Leer hora
	Escribir "Ingrese la cantidad de horas en las que desea saber la hora:  "
	Leer cant
	
	horaNueva = (hora + cant) Mod 24
	Imprimir "La hora después de ", cant, "horas, será:  ", horaNueva
FinAlgoritmo
