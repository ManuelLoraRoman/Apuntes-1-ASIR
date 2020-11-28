
Proceso Ejercicio_9
	
	Definir num1,num2,num3,pos1,pos2,pos3 como Real;
	
	Escribir Sin Saltar "Escriba el primer nº: ";
	
	Leer num1;
	
	Escribir Sin Saltar "Escriba el segundo nº: ";
	
	Leer num2;
	
	Escribir Sin Saltar "Escriba el tercer nº: ";
	
	Leer num3;
	
	Si num1 > num2 y num1 > num3 Entonces
		
		pos1 <- num1;
		
		Si num2 > num3 Entonces
			
			pos2 <- num2;
			
			pos3 <- num3;
			
			Escribir "El orden de mayor a menor sería: ", pos1 , " > ", pos2 , " > " , pos3 , ".";
			
		SiNo
			
			pos2 <- num3;
			
			pos3 <- num2;
			
			Escribir "El orden de mayor a menor sería: ", pos1 , " > ", pos2 , " > " , pos3 , ".";
			
		FinSi
		
	SiNo
		
		Si num2 > num1 y num2 > num3 Entonces
			
			pos1 <- num2;
			
			Si num1 > num3 Entonces
				
				pos2 <- num1;
				
				pos3 <- num3;
				
				Escribir "El orden de mayor a menor sería: ", pos1 , " > ", pos2 , " > " , pos3 , ".";
				
			SiNo
				
				pos2 <- num3;
				
				pos3 <- num1;
				
				Escribir "El orden de mayor a menor sería: ", pos1 , " > ", pos2 , " > " , pos3 , ".";
				
			FinSi
			
		SiNo
			
			pos1 <- num3;
			
			Si num1 > num2 Entonces
				
				pos2 <- num1;
				
				pos3 <- num2;
				
				Escribir "El orden de mayor a menor sería: ", pos1 , " > ", pos2 , " > " , pos3 , ".";
				
			SiNo
				
				pos2 <- num2;
				
				pos3 <- num1;
				
				Escribir "El orden de mayor a menor sería: ", pos1 , " > ", pos2 , " > " , pos3 , ".";
				
			FinSi
			
		FinSi
		
	FinSi
	
FinProceso
