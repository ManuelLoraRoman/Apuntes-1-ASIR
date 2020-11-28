
Proceso Ejercicio_6
	
	Definir cad,carac,cad1,cad2 como Cadena;
	
	Definir n,m Como Real;
	
	n <- 0;
	
	m <- 0;
	
	cad1 <- "";
	
	cad <- "";
	
	Escribir "Escriba caracteres para formar una palabra (para terminar pulsa espacio): ";
	
	Repetir
		
		Leer carac;
		
		Si carac = " " Entonces
			
			cad <- cad;
			
		SiNo
			
			cad <- Concatenar(cad,carac);
			
		FinSi
		
		n <- n + 1;
		
	Hasta Que carac = " "
	
	Para m <- 0 Hasta Longitud(cad) + 1 Hacer
		
		cad2 <- Subcadena(cad,n-m,n-m);
		
		cad1 <- Concatenar(cad1,cad2);
		
	FinPara
	
	Escribir "La palabra sería: ", cad , "."; 
	
	Escribir "La palabra invertida sería: ", cad1 , "."; 
	
	
FinProceso
