
Proceso Ejercicio_6
	
	Definir num1,num2,n Como Real;
	
	Escribir Sin Saltar "Escribe el primer número: ";
	
	Leer num1;
	
	Escribir Sin Saltar "Escribe el segundo número";
	
	Leer num2;
	
	n <- 0;
	
	Repetir
		
		Si num1 % 2 = 0 Entonces
			
			n <- n + 1;
			
		SiNo
			
			n <- n + 0;
			
		FinSi
		
		Si num2 % 2 = 0 Entonces
			
			n <- n + 2;
			
		SiNo
			
			n <- n + 0;
			
		FinSi
		
	Hasta Que n >= 0 Y n <=3
	
	Escribir "PARES:";
	
	Escribir "------";
	
	Si n = 0 Entonces
		
		Escribir "No hay números pares";
		
	SiNo
		
		Si n = 1 Entonces
			
			Escribir num1;
			
		SiNo
			
			Si n = 2 Entonces
				
				Escribir num2;
				
			SiNo
				
				Escribir num1;
				
				Escribir num2;
				
			FinSi
			
		FinSi
		
	FinSi
	
FinProceso
