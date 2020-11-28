
Proceso Ejercicio_3
	
	//Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
	//A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
	
	Definir vector_nota,i,nota,notamed como Entero;
	
	Dimension vector_nota[5];
	
	notamed <- 0;
	
	Para i <- 0 Hasta 4 Hacer
		
		Escribir "Escribe la ", i , "º nota del alumno: ";
		
		Leer nota;
		
		vector_nota[i] <- nota;
		
		notamed <- notamed + nota;
		
	FinPara
	
	Escribir "Todas las notas serían: "; 
	
	Para i <- 0 hasta 4 Hacer
		
		Escribir vector_nota[i];
		
	FinPara
	
	i <- 0;

	Si vector_nota[i] < vector_nota[i + 1] Y vector_nota[i] < vector_nota[i + 2] Y vector_nota[i] < vector_nota[i + 3] Y vector_nota[i] < vector_nota[i + 4] Entonces
		
		Escribir "La nota más baja es: ", vector_nota[i] , ".";
		
	SiNo
		
		Si vector_nota[i + 1] < vector_nota[i] Y vector_nota[i + 1] < vector_nota[i + 2] Y vector_nota[i + 1] < vector_nota[i + 3] Y vector_nota[i + 1] < vector_nota[i + 4] Entonces
			
			Escribir "La nota más baja es: ", vector_nota[i + 1] , ".";
			
		SiNo
			
			Si vector_nota[i + 2] < vector_nota[i] Y vector_nota[i + 2] < vector_nota[i + 1] Y vector_nota[i + 2] < vector_nota[i + 3] Y vector_nota[i + 2] < vector_nota[i + 4] Entonces
				
				Escribir "La nota más baja es: ", vector_nota[i + 2] , ".";
				
			SiNo
				
				Si vector_nota[i + 3] < vector_nota[i] Y vector_nota[i + 3] < vector_nota[i + 1] Y vector_nota[i + 3] < vector_nota[i + 2] Y vector_nota[i + 3] < vector_nota[i + 4] Entonces
					
					Escribir "La nota más baja es: ", vector_nota[i + 3] , ".";
					
				SiNo
					
					Escribir "La nota más baja es: ", vector_nota[i + 4] , ".";
					
				FinSi
				
			FinSi
			
		FinSi
		
	FinSi
	
	
	

	
	Si vector_nota[i] > vector_nota[i + 1] Y vector_nota[i] > vector_nota[i + 2] Y vector_nota[i] > vector_nota[i + 3] Y vector_nota[i] > vector_nota[i + 4] Entonces
		
		Escribir "La nota más alta es: ", vector_nota[i] , ".";
		
	SiNo
		
		Si vector_nota[i + 1] > vector_nota[i] Y vector_nota[i + 1] > vector_nota[i + 2] Y vector_nota[i + 1] > vector_nota[i + 3] Y vector_nota[i + 1] > vector_nota[i + 4] Entonces
			
			Escribir "La nota más alta es: ", vector_nota[i + 1] , ".";
			
		SiNo
			
			Si vector_nota[i + 2] > vector_nota[i] Y vector_nota[i + 2] > vector_nota[i + 1] Y vector_nota[i + 2] > vector_nota[i + 3] Y vector_nota[i + 2] > vector_nota[i + 4] Entonces
				
				Escribir "La nota más alta es: ", vector_nota[i + 2] , ".";
				
			SiNo
				
				Si vector_nota[i + 3] > vector_nota[i] Y vector_nota[i + 3] > vector_nota[i + 1] Y vector_nota[i + 3] > vector_nota[i + 2] Y vector_nota[i + 3] > vector_nota[i + 4] Entonces
					
					Escribir "La nota más alta es: ", vector_nota[i + 3] , ".";
					
				SiNo
					
					Escribir "La nota más alta es: ", vector_nota[i + 4] , ".";
					
				FinSi
				
			FinSi
			
		FinSi
		
	FinSi
	
	
	Escribir "La nota media sería: ", notamed / 5 , ".";
	
FinProceso
