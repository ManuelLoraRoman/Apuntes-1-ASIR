
Proceso Ejercicio_17
	
	Definir num como Real;
	
	Definir numtxt como Cadena;
	
	Escribir "Lanzas un dado";
	
	num <- azar(6 + 1);
	
	Escribir "Su número es: " , num , ".";
	
	Si num = 1 Entonces
		
		numtxt <- "seis";
		
		Escribir "En la cara opuesta está el ", numtxt , ".";
		
	SiNo
		
		Si num = 6 Entonces
			
			numtxt <- "uno";
			
			Escribir "En la cara opuesta está el ", numtxt , ".";
			
		SiNo
			
			Si num = 2 Entonces
				
				numtxt <- "cinco";
				
				Escribir "En la cara opuesta está el ", numtxt , ".";
				
			SiNo
				
				Si num = 5 Entonces
					
					numtxt <- "dos";
					
					Escribir "En la cara opuesta está el ", numtxt , ".";
					
				SiNo
					
					Si num = 3 Entonces
						
						numtxt <- "cuatro";
						
						Escribir "En la cara opuesta está el ", numtxt , ".";
						
					SiNo
						
						numtxt <- "tres";
						
						Escribir "En la cara opuesta está el ", numtxt , ".";
						
					FinSi
					
				FinSi
				
			FinSi
			
		FinSi
		
	FinSi
	
FinProceso
