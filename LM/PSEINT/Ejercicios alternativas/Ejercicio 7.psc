
Proceso Ejercicio_7
	
	Definir base,expo como Real;
	
	Escribir Sin Saltar "Escriba la base de su potencia: ";
	
	Leer base;
	
	Escribir Sin Saltar "Escriba el exponente de su potencia: ";
	
	Leer expo;
	
	Si expo > 0 Entonces
		
		Escribir "La potencia sería: ",base," ^ ",expo," y su solución es ", base ^ expo , ".";
		
	SiNo
		
		Si expo = 0 Entonces
			
			Escribir "La potencia sería: ",base," ^ ",expo," y su solución es ", base ^ expo , ".";
			
		SiNo
			
			Escribir "La potencia sería: ",base," ^ ",expo," y su solución es ", (base ^ expo), ".";
			
		FinSi
	FinSi
	
FinProceso
