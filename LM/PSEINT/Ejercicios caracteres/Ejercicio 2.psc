
Proceso Ejercicio_2
	
	Definir subcad,subcad1,cad como Cadena;
	
	Escribir Sin Saltar "Escriba algo: ";
	
	Leer cad;
	
	Escribir Sin Saltar "Escriba algo para comprobar subcadenas: ";
	
	Leer subcad;
	
	subcad1 <- Subcadena(cad,0,Longitud(subcad) - 1);
	
	Si subcad != subcad1 Entonces
		
		Escribir "No está incluida la subcadena";
		
	SiNo
		
		Escribir "Sí está incluida la subcadena";
		
	FinSi
	
FinProceso
