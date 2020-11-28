
Proceso Ejercicio_8
	
	Definir nota,edad como Real;
	
	Definir sexo Como Caracter;
	
	Escribir Sin Saltar "Escriba su nota: ";
	
	Leer nota;
	
	Escribir Sin Saltar "Escriba su edad: ";
	
	Leer edad;
	
	Escribir Sin Saltar "Escriba su sexo(M/F): ";
	
	Leer sexo;
	
	Si nota >= 5 Entonces
		
		Si edad >= 18 Entonces
			
			Si sexo = "F" o sexo = "f" Entonces
				
				Escribir "ACEPTADA";
				
			SiNo 
				
				Si sexo = "M" o sexo = "m" Entonces
					
					Escribir "POSIBLE";
					
				SiNo
					
					Escribir "NO ACEPTADA";
					
				FinSi
				
				
				
			FinSi
			
		SiNo
			
			Escribir "NO ACEPTADA";
			
		FinSi
		
	SiNo
		
		Escribir "NO ACEPTADA";
		
	FinSi
	
FinProceso
