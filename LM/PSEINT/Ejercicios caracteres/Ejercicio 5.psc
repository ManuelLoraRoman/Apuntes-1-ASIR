
Proceso Ejercicio_5
	
	Definir cad,cad1 como Cadena;
	
	Definir es_espacio como Logico;
	
	Definir n como Real;
	
	Escribir Sin Saltar "Escribe tu nombre: ";
	
	Leer cad;
	
	n <- 0;
	
	es_espacio <- falso;
	
	cad1 <- Subcadena(cad,0,0);
	
	Para n <- 0 Hasta Longitud(cad) Hacer
		
		Si Subcadena(cad,n,n) = " " Entonces
			
			es_espacio <- verdadero;
			
		FinSi
		
		Si es_espacio Entonces
			
			cad1 <- Concatenar(cad1,Subcadena(cad,n + 1,n + 1));
			
			es_espacio <- falso;
			
		FinSi
		
	FinPara
	
	Escribir "Las iniciales serían ", cad1 ,".";
	
FinProceso
