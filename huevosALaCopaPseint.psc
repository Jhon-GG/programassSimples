Algoritmo huevosALaCopa
	Definir m1, m2, dens, c, k, tw, tempO, m, ty, t Como Real
	
    m1 = 47
    m2 = 67
    dens = 1.038
    c = 3.7
    k = 5.4 * 10^(-3)   // Notación científica sin "e"
    tw = 100
	
    Escribir "Ingrese la temperatura original del huevo en grados celsius: "
    Leer tempO
	
    m = m1 
	
    ty = 70
    t = (m^(2/3) * c * dens^(1/3)) / (k * Pi^(4*3.1416/3)^(2/3)) * (Ln(0.76 * (tempO - tw) / (tempO - tw - 100)) / Ln(10))
	
    Escribir "El tiempo necesario para alcanzar la temperatura máxima (", ty, "°C) y preparar el huevo a la copa es de ", t, " segundos."

FinAlgoritmo
