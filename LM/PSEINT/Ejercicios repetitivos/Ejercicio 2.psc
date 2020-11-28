
Proceso Ejercicio_2
	
	Definir num,inten,resp Como Real;
	
	Escribir "Adivina el número que estoy pensando ^-^";
	
	num <- aleatorio(0,101);
	
	Escribir Sin Saltar "Escribe el número: ";
	
	Leer resp;
	
	inten <- 1;
	
	Mientras resp <> num Hacer
		
		Si resp > num Entonces
			
			Escribir "El número introducido es mayor que el pensado. Vuelva a intentarlo.";
			
			inten <- inten + 1;
			
			Escribir "";
			
			Escribir "Adivina el número que estoy pensando ^-^";
			
			Leer resp;
			
		SiNo
			
			Escribir "El número introducido es menor que el pensado. Vuelva a intentarlo.";
			
			inten <- inten + 1;
			
			Escribir "";
			
			Escribir "Adivina el número que estoy pensando ^-^";
			
			Leer resp;
			
		FinSi
		
	FinMientras
	
	Si inten >= 11 Entonces
		
		Escribir "No has acertado el número en los 10 intentos dados. Reinicia el programa para volver a intentarlo";
		
	SiNo
		
		Escribir "Has acertado el número en ", inten , " intentos.";
		
	FinSi
	
FinProceso
