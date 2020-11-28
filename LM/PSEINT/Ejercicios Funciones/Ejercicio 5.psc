
//Crea una funci�n "calcularMaxMin" que recibe una arreglo con valores num�rico y devuelve el valor m�ximo y el m�nimo.
//Crea un programa que pida n�meros por teclado y muestre el m�ximo y el m�nimo, utilizando la funci�n anterior.

Funcion calc <- calcularMaxMin(vector_num,tamano,maxrefer,minrefer)
	
	Definir n como Entero;
	
	maxrefer <- vector_num[0];
	
	minrefer <- vector_num[0];
	
	Para n <- 0 Hasta tamano - 1 Hacer
		
		Si maxrefer < vector_num[n] Entonces
			
			maxrefer <- vector_num[n];
			
		FinSi
		
		Si minrefer > vector_num[n] Entonces
			
			minrefer <- vector_num[n];
			
		FinSi
		
	FinPara
	
FinFuncion

Proceso MaxMin
	
	Definir lista,minmax Como Entero;
	
	Dimension lista[10];
	
	Definir tamano_lista,i Como Entero;
	
	Definir vmax,vmin como Entero;
	
	tamano_lista <- 10;
	
	Para i <- 0 hasta tamano_lista - 1 Hacer
		
		lista[i] <- Aleatorio(1,100);
		
	FinPara
	
	minmax <- calcularMaxMin(lista,tamano_lista,vmax,vmin);
	
	Escribir "El valor m�ximo es ",vmax;
	
	Escribir "El valor m�nimo es ",vmin;
	
FinProceso
