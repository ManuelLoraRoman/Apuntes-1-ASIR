
Proceso Ejercicio_8
	
	Definir liminf,limsup,n,sum,num como Real;
	
	Definir igual Como Logico;
	
	n <- 0;
	
	sum <- 0;
	
	Escribir Sin Saltar "Escribe el l�mite superior: ";
	
	Leer limsup;
	
	Repetir
		
		Escribir Sin Saltar "Escribe el l�mite inferior: ";
		
		Leer liminf;
		
		Si liminf > limsup Entonces
			
			Escribir "�ERROR! El l�mite inferior debe ser menor que el superior.";
			
		FinSi
		
	Hasta Que liminf <= limsup
	
	Repetir
		
		Escribir Sin Saltar "Escribe un n�mero: ";
		
		Leer num;
		
		Si num > liminf Y num < limsup Entonces
			
			sum <- sum + num;
			
		SiNo
			
			Si num < liminf O num > limsup Entonces
				
				n <- n + 1;
				
			SiNo
				
				igual <- Verdadero;
				
			FinSi
			
		FinSi
		
	Hasta Que num = 0
	
	Escribir "1) La suma de los n�s dentro del intervalo es: ", sum , ".";
	
	Escribir "2) Hay ", n , " n�meros fuera del intervalo.";
	
	Si igual = verdadero Entonces
		
		Escribir "3) Se ha introducido un n�mero igual a alg�n intervalo.";
		
	SiNo
		
		Escribir "3) No se ha introducido un n�mero igual a alg�n intervalo.";
		
	FinSi
	
FinProceso
