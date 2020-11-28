
Proceso Ejercicio_18
	
	Definir dia como Real;
	
	Repetir
		
		Escribir Sin Saltar "Escriba el dia de la semana (1-7): ";
		
		Leer dia;
		
		Si dia <= 0 O dia > 7 Entonces
			
			Escribir "¡ERROR! Introduzca nuevamente el dia.";
			
		FinSi
		
	Hasta Que dia >= 1 Y dia <= 7
	
	Si dia = 1 Entonces
		
		Escribir "El dia de la semana es lunes.";
		
	SiNo
		
		Si dia = 2 Entonces
			
			Escribir "El dia de la semana es martes.";
			
		SiNo
			
			Si dia = 3 Entonces
				
				Escribir "El dia de la semana es miércoles.";
				
			SiNo
				
				Si dia = 4 Entonces
					
					Escribir "El dia de la semana es jueves.";
					
				SiNo
					
					Si dia = 5 Entonces
						
						Escribir "El dia de la semana es viernes.";
						
					SiNo
						
						Si dia = 6 Entonces
							
							Escribir "El dia de la semana es sábado.";
							
						SiNo
							
							Escribir "El día de la semana es domingo.";
							
						FinSi
						
					FinSi
					
				FinSi
				
			FinSi
			
		FinSi
		
	FinSi
	
FinProceso
