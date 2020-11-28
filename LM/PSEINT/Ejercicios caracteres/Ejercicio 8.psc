
Proceso Ejercicio_8
	
	Definir cad,cad1 como Cadena;
	
	Definir n como Real;
	
	Escribir Sin Saltar "Escribe una palabra (puede incluir mayúsculas y minúsculas): ";
	
	Leer cad;
	
	n <- 0;
	
	cad1 <- "";
	
	Para n <- 0 Hasta Longitud(cad) + 1 Hacer
		
		Si Subcadena(cad,n,n) = Mayusculas(Subcadena(cad,n,n)) Entonces
			
			cad1 <- Concatenar(cad1,Minusculas(Subcadena(cad,n,n)));
			
		SiNo
			
			cad1 <- Concatenar(cad1,Mayusculas(Subcadena(cad,n,n)));
			
		FinSi
		
	FinPara
	
	Escribir "La conversión sería: ", cad1 , ".";
	
FinProceso
