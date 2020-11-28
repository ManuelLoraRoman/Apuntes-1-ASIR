
Proceso Ejercicio_10
	
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
	
	Si cad1 = cad Entonces
		
		Escribir "La palabra es palindroma.";
		
	SiNo
		
		Escribir "La palabra no es palindroma.";
		
	FinSi
	
FinProceso
