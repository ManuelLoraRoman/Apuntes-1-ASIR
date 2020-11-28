
Proceso Ejercicio_14
	
	Definir tipo,tama Como Cadena;
	
	Definir precioinic,total Como Real;
	
	Escribir Sin Saltar "¿Cuántos kilos de uva quieres?: ";
	
	Leer precioinic;
	
	Escribir Sin Saltar "¿Qué tipo de uva desea (A/B): ";
	
	Leer tipo;
	
	Escribir Sin Saltar "¿Qué tamaño de uva desea (1/2): ";
	
	Leer tama;
	
	Si tama = "1" Entonces
		
		Si tipo = "A" O tipo = "a" Entonces
			
			Escribir "La ganancia obtenida sería de ", precioinic + (0.20 * precioinic) , " euros.";
			
		SiNo
			
			Escribir "La ganancia obtenida sería de ", precioinic - (0.30 * precioinic), " euros.";
			
		FinSi
		
	SiNo
		
		Si tipo = "A" O tipo = "a" Entonces
			
			Escribir "La ganancia obtenida sería de ", precioinic + (0.30 * precioinic), " euros.";
			
		SiNo
			
			Escribir "La ganancia obtenida sería de ", precioinic - (0.50 * precioinic), " euros.";
			
		FinSi
		
	FinSi
	
FinProceso
