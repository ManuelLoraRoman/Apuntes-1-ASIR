
Proceso Ejercicio_1
	
	Definir cad como Cadena;
	
	Definir n,L como Real;
	
	Escribir Sin Saltar "Escribe algo: ";
	
	Leer cad;
	
	n <- 0;
	
	L <- Longitud(cad);
	
	Escribir "Estos son todos los carácteres de la cadena: ";
	
	Repetir
		
		Si n != L Entonces
			
			Escribir Sin Saltar Subcadena(cad,n,n), "-";
			
		SiNo
			
			Escribir Sin Saltar Subcadena(cad,n,n);
			
		FinSi
		
		n <- n + 1;
		
	Hasta Que n = L 
	
FinProceso
