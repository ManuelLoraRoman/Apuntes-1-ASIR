
Proceso Ejercicio_7
	
	// Programa que declare tres vectores 'vector1', 'vector2' y 'vector3' de cinco enteros cada uno, pida valores para 'vector1' y 'vector2' y calcule vector3=vector1+vector2.
	
	Definir vector1,vector2,vector3,i como Entero;
	
	Dimension vector1[5],vector2[5],vector3[5];
	
	Para i <- 0 Hasta 4 Hacer
		
		Escribir Sin Saltar "Escribe el " , i , "º número del vector 1: ";
		
		Leer vector1[i];
		
	FinPara
	
	i <- 0;
	
	Para i <- 0 Hasta 4 Hacer
		
		Escribir Sin Saltar "Escribe el " , i , "º número del vector 2: ";
		
		Leer vector2[i];
		
	FinPara
	
	i <- 0;
	
	Para i <- 0 Hasta 4 Hacer
		
		Escribir "Este es el vector 3 suma de los anteriores";
		
		vector3[i] <- vector1[i] + vector2[i];
		
		Escribir vector3[i];
		
	FinPara
	
	
FinProceso
