
Proceso Ejercicio_11
	
	Definir num,n,m,div como Real;
	
	Escribir Sin Saltar "Escribe un n�mero: ";
	
	Leer num;
	
	n <- 1;
	
	m <- 0;
	
	div <- 0;
	
	Repetir
		
		Si num % n = 0 Entonces
			
			div <- div + 1;
			
		FinSi
		
		n <- n + 1;
		
		m <- m + 1;
		
	Hasta Que m = num
	
	Si div = 2 O num = 1 Entonces
		
		Escribir "El n�mero ", num , " es primo.";
		
	SiNo
		
		Escribir "El n�mero ", num , " no es primo.";
		
	FinSi
	
FinProceso
