
Proceso Ejercicio_4
	
	//Programa que declare un vector de diez elementos enteros y pida números para rellenarlo hasta que se llene el vector o se introduzca un número negativo. 
	//Entonces se debe imprimir el vector (sólo los elementos introducidos).
	
	Definir vector_enteros,num,n,i como Enteros;
	
	Dimension vector_enteros[10];
	
	i <- 0;
	
	n <- 0;
	
	Repetir
		
		Escribir "Escribe un número: ";
		
		Leer num;
		
		vector_enteros[i] <- num;
		
		i <- i + 1;
		
		n <- n + 1;ffff
		
	Hasta Que n = 10 O num < 0
	
	i <- 0;
	
	Escribir "Los números del vector serían: ";
	
	Mientras n <> 0 Hacer
		
		Escribir vector_enteros[i];
		
		i <- i + 1;
		
		n <- n - 1;
		
	FinMientras
	
FinProceso
