Algoritmo numeroInvertido
	Definir _num, _uni, _dec, _cen como Real
	Escribir "Ingrese un numero de tres digitos:  "
	Leer _num
	
	_cen <- _num MOD 10 - 2
	_dec <- (_num MOD 100) MOD 10 - 1
	_uni <- _num MOD 10
	Imprimir  "El numero  ", _num, "invertido seria:  ", _uni, _dec, _cen 
FinAlgoritmo
