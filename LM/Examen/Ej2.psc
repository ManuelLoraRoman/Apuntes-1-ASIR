
Proceso Ejercicio_2
	
	Definir coefa,coefb,resultado como Real;
	
	Escribir "Dada la ecuaci�n de primer grado : ax + b = 0 ";
	
	Escribir Sin Saltar "Escriba el coeficiente a: ";
	
	Leer coefa;
	
	Escribir Sin Saltar "Escriba el coeficiente b: ";
	
	Leer coefb;
	
	Escribir "Coeficiente a: ", coefa;
	
	Escribir "Coeficiente b: ",coefb;
	
	Si coefa = 0 && coefb <> 0 Entonces
		
		Escribir "No tiene soluci�n.";
		
	SiNo
		
		Si coefa = 0 && coefb = 0 Entonces
			
			Escribir "Infinitas soluciones.";
			
		SiNo
			
			resultado <- -coefb / coefa;
			
			Escribir "Soluci�n: ", resultado, ".";
			
		FinSi
		
	FinSi
	
FinProceso
