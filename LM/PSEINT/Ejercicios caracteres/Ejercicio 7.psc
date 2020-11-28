
Proceso Ejercicio_7
	
	Definir cad,cad1,cad2,cad3 como Cadena;
	
	Definir carac1,carac2 como Caracter;
	
	Definir n,L como Real;
	
	Escribir Sin Saltar "Escriba una palabra: ";
	
	Leer cad;
	
	Escribir Sin Saltar "Escriba un caracter: ";
	
	Leer carac1;
	
	Escribir Sin Saltar "Escriba un segundo caracter: ";
	
	Leer carac2;
	
	n <- 0;
	
	L <- 0;
	
	cad3 <- "";
	
	Para n <- 0 Hasta Longitud(cad) + 1 Hacer
		
		Si L = 0 Entonces
			
			Si Subcadena(cad,n,n) = carac1 Entonces
				
				cad1 <- Subcadena(cad,0,n - 1);
				
				cad2 <- Subcadena(cad,n + 1,Longitud(cad));
				
				carac1 <- carac2;
				
				cad3 <- Concatenar(cad3,cad1);
				
				cad3 <- Concatenar(cad3,carac1);
				
				cad3 <- Concatenar(cad3,cad2);
				
				L <- 1;
				
			FinSi
			
		FinSi
		
	FinPara
	
	Escribir "La cadena nueva sería: ", cad3 , ".";
	
FinProceso
