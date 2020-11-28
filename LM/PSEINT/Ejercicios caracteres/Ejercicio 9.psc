
Proceso Ejercicio_9
	
	Definir cad,subcad como Cadena;
	
	Definir n Como Real;
	
	Definir si_contiene como Logico;
	
	Escribir Sin Saltar "Escriba una palabra: ";
	
	Leer cad;
	
	Escribir Sin Saltar "Escriba lo que quieres comprobar: ";
	
	Leer subcad;
	
	si_contiene <- falso;
	
	n <- Longitud(cad) - Longitud(subcad) + 1;
	
	Para n <- 0 Hasta n - 1 Hacer
		
		Si Subcadena(cad , n , n + Longitud(subcad)- 1) = subcad Entonces
			
			si_contiene <- verdadero;
			
		FinSi
		
	FinPara
	
	Si si_contiene Entonces
		
		Escribir "La palabra si contiene la subcadena.";
		
	SiNo
		
		Escribir "La palabra no contiene la subcadena.";
		
		
	FinSi
	
	
	
FinProceso
