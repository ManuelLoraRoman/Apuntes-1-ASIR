
Proceso Ejercicio_15
	
	Definir alum,precio Como Real;
	
	Escribir Sin Saltar "Escriba el nº total de alumnos";
	
	Leer alum;
	
	Si alum >= 100 Entonces
		
		precio <- alum * 65;
		
		Escribir Sin Saltar "El precio por alumno es 65 y hay que pagar a la compañia ";
		
		Escribir precio, ".";
		
	SiNo
		
		Si alum >=50 Y alum <= 99 Entonces
			
			precio <- alum * 70;
			
			Escribir Sin Saltar "El precio por alumno es 70 y hay que pagar a la compañia ";
			
			Escribir precio, ".";
			
		SiNo
			
			Si alum >= 30 Y alum <= 49 Entonces
				
				precio <- alum * 95;
				
				Escribir Sin Saltar "El precio por alumno es 95 y hay que pagar a la compañia ";
				
				Escribir precio, ".";
				
			SiNo
				
				Escribir Sin Saltar "El precio por ", alum , " alumnos es de 4000 euros.";
				
			FinSi
			
			
		FinSi
		
		
	FinSi
	
FinProceso
