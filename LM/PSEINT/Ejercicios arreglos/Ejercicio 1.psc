
Proceso Ejercicio_1
	
	Definir vector_numeros como Entero;
	
	Definir i como Entero;
	
	Dimension vector_numeros[10];
	
	Para i <- 0 Hasta 9 Hacer
		
		vector_numeros[i] <- azar(10);
		
	FinPara
	
	Para i <- 0 Hasta 9 Hacer
		
		Escribir "El número sacado al azar es: ",vector_numeros[i], " .Su cuadrado: " , vector_numeros[i] ^ 2, " y su Cubo:" , vector_numeros[i] ^ 3, ".";
		
	FinPara
	
FinProceso
