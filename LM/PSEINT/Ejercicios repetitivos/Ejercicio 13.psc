
Proceso Ejercicio_13
	
	Definir sueldo,n,horas,dinerob,totalh como Real;
	
	Escribir Sin Saltar "Dinero base por hora trabajada: ";
	
	Leer dinerob;
	
	n <- 1;
	
	horas <- 0;
	
	totalh <- 0;
	
	Repetir
		
		Segun n Hacer
			
			1:
				
				Escribir Sin Saltar "Horas trabajadas el lunes: ";
				
			2:
				
				Escribir Sin Saltar "Horas trabajadas el martes: ";
				
			3:
				
				Escribir Sin Saltar "Horas trabajadas el miercóles: ";
				
			4:
				
				Escribir Sin Saltar "Horas trabajadas el jueves: ";
				
			5:
				
				Escribir Sin Saltar "Horas trabajadas el viernes: ";
				
			De Otro Modo:
				
				Escribir Sin Saltar "Horas trabajadas el sábado: ";
				
		FinSegun
		
		Leer horas;
		
		totalh <- totalh + horas;
		
		n <- n + 1;
		
	Hasta Que n = 7
	
	sueldo <- totalh * dinerob;
	
	Escribir "El total de horas trabajadas será: ", totalh ,".";
	
	Escribir "El sueldo recibido por las horas trabajadas ", sueldo , ".";
	
FinProceso
