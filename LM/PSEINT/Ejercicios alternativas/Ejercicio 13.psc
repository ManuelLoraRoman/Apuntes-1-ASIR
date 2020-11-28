
Proceso Ejercicio_13
	
	Definir dd,mm,yyyy Como Real;
	
	Repetir
		
		Escribir Sin Saltar "Escriba el día deseado: ";
		
		Leer dd;
		
		Si dd < 1 O dd >= 32 Entonces
			
			Escribir "El día introducido es incorrecto. Se iniciará de nuevo el programa.";
			
		FinSi
		
	Hasta Que dd >= 1 Y dd <= 31
	
	Repetir
		
		Repetir
			
			Escribir Sin Saltar "Escriba el mes deseado: ";
			
			Leer mm;
			
			Si mm = 2 Y dd > 28 Entonces
				
				Escribir "El mes introducido es incorrecto. Ponga de nuevo el mes.";
				
				
			SiNo
				
				Si mm < 1 O mm >= 13 Entonces
					
					Escribir "El mes introducido es incorrecto. Ponga de nuevo el mes.";
					
				FinSi
				
			FinSi
			
		Hasta Que mm >= 1 Y mm <= 12
		
	Hasta que mm != 2	
	
	Repetir
		
		Escribir Sin Saltar "Escriba el año deseado: ";
		
		Leer yyyy;
		
		Si yyyy < 1990 O yyyy >= 2099 Entonces
			
			Escribir "El año introducido es incorrecto. Introduzca el año nuevamente.";
			
		FinSi
		
	Hasta Que yyyy >= 1990 Y yyyy <= 2099
	
	Escribir "El año introducido ", dd , "/", mm , "/" , yyyy , " es correcta.";
	
	
FinProceso
