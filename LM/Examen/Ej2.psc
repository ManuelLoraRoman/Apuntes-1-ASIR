
Proceso Ejercicio_2
	
	Definir coefa,coefb,resultado como Real;
	
	Escribir "Dada la ecuación de primer grado : ax + b = 0 ";
	
	Escribir Sin Saltar "Escriba el coeficiente a: ";
	
	Leer coefa;
	
	Escribir Sin Saltar "Escriba el coeficiente b: ";
	
	Leer coefb;
	
	Escribir "Coeficiente a: ", coefa;
	
	Escribir "Coeficiente b: ",coefb;
	
	Si coefa = 0 && coefb <> 0 Entonces
		
		Escribir "No tiene solución.";
		
	SiNo
		
		Si coefa = 0 && coefb = 0 Entonces
			
			Escribir "Infinitas soluciones.";
			
		SiNo
			
			resultado <- -coefb / coefa;
			
			Escribir "Solución: ", resultado, ".";
			
		FinSi
		
	FinSi
	
FinProceso
