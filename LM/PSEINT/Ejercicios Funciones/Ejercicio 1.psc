

Funcion EscribirCentrado(cad)
	
	Definir n,i como Real;
	
	n <- 0;
	
	Mientras n <> (40 - (Longitud(cad)/2)) Hacer
		
		Escribir Sin Saltar " ";
		
		n <- n + 1;
		
	FinMientras
	
	Escribir cad;
	
	Para i <- 0 hasta (40 + (Longitud(cad)/2)) Hacer
		
		Si i < (40 - (Longitud(cad)/2)) Entonces
			
			Escribir Sin Saltar " ";
			
		SiNo
			
			Escribir Sin Saltar "-";
			
		FinSi
		
	FinPara
	
FinFuncion
	
Proceso Centros
	
	Definir centro como Cadena;
	
	Leer centro;
	
	EscribirCentrado(centro);
	
	Escribir "";
	
FinProceso
