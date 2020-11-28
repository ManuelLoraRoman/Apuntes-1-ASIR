
Proceso Ejercicio_5
	
	//Hacer un programa que inicialice un vector de números con valores aleatorios, y posterior ordene los elementos de menor a mayor.
	
	Definir vector_num,vector_num1,i,n Como Entero;
	
	Dimension vector_num[10];
	
	Dimension vector_num1[10];
	
	Para i <- 0 Hasta 9 Hacer
		
		vector_num[i] <- aleatorio(0,9);
		
	FinPara
	
	i <- 0;
	
	Para i <- 0 Hasta 9 Hacer
		
		Si vector_num[i] > vector_num[i + 1] Entonces
			
			vector_num1[i] <- vector_num[i + 1];
			
			vector_num1[i + 1] <- vector_num[i + 1];
			
		FinSi
		
	FinPara
	
	i <- 0;
	
	Escribir Sin Saltar "Ordenados de menor a mayor";
	
	Para i <- 0 hasta 9 Hacer
		
		Escribir Sin Saltar vector
		
	FinPara
	
	
FinProceso
