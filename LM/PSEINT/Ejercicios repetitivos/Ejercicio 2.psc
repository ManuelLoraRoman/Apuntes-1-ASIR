
Proceso Ejercicio_2
	
	Definir num,inten,resp Como Real;
	
	Escribir "Adivina el n�mero que estoy pensando ^-^";
	
	num <- aleatorio(0,101);
	
	Escribir Sin Saltar "Escribe el n�mero: ";
	
	Leer resp;
	
	inten <- 1;
	
	Mientras resp <> num Hacer
		
		Si resp > num Entonces
			
			Escribir "El n�mero introducido es mayor que el pensado. Vuelva a intentarlo.";
			
			inten <- inten + 1;
			
			Escribir "";
			
			Escribir "Adivina el n�mero que estoy pensando ^-^";
			
			Leer resp;
			
		SiNo
			
			Escribir "El n�mero introducido es menor que el pensado. Vuelva a intentarlo.";
			
			inten <- inten + 1;
			
			Escribir "";
			
			Escribir "Adivina el n�mero que estoy pensando ^-^";
			
			Leer resp;
			
		FinSi
		
	FinMientras
	
	Si inten >= 11 Entonces
		
		Escribir "No has acertado el n�mero en los 10 intentos dados. Reinicia el programa para volver a intentarlo";
		
	SiNo
		
		Escribir "Has acertado el n�mero en ", inten , " intentos.";
		
	FinSi
	
FinProceso
