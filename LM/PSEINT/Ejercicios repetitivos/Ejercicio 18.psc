
Proceso Ejercicio_18
	
	Definir hh,mm,ss como Real;
	
	Definir res como Cadena;
	
	hh <- 0;
	
	mm <- 0;
	
	ss <- 0;
	
	res <- "S";
	
	Mientras res = "S" Hacer
		
		Mientras hh < 24 Hacer
			
			Mientras mm < 60 Hacer
				
				Mientras ss < 60 Hacer
					
					Escribir hh , ":" , mm , ":" , ss;
					
					Esperar 1 Segundos;
					
					ss <- ss + 1;
					
					Borrar Pantalla;
					
				FinMientras
				
				mm <- mm + 1;
				
				ss <- 0;
				
			FinMientras
			
			hh <- hh + 1;
			
			mm <- 0;
			
		FinMientras
		
		hh <- 0;
		
	FinMientras
	
FinProceso
