
Proceso Ejercicio_4
	
	Definir extremoinf,extremosup,num,media,i,n como Entero;
	
	Definir es_igual como Logico;
	
	es_igual <- falso;
	
	media <- 0;
	
	i <- 0;
	
	n <- 0;
	
	Escribir Sin Saltar "Escriba el extremo inferior de un intervalo: ";
	
	Repetir
		
		Leer extremoinf;
		
		Si extremoinf < 0 Entonces
			
			Escribir Sin Saltar "�ERROR! El n�mero introducido es negativo. Escriba otro n�mero: ";
			
		FinSi
		
	Hasta Que extremoinf > 0
	
	Escribir Sin Saltar "Escriba el extremo superior de un intervalo: ";
	
	Repetir
		
		Leer extremosup;
		
		Si extremosup < 0 Entonces
			
			Escribir Sin Saltar "�ERROR! El n�mero introducido es negativo. Escriba otro n�mero: ";
			
		SiNo
			
			Si extremosup < extremoinf Entonces
				
				Escribir Sin Saltar "�ERROR! El extremo inferior debe ser menor que el extremo superior. Escriba otro n�mero: ";
				
			FinSi	
			
		FinSi
		
	Hasta Que extremosup > 0 && extremosup > extremoinf
	
	Repetir
		
		Escribir Sin Saltar "Escriba un n�mero para su comprobaci�n: ";
		
		Leer num;
		
		Si num = extremoinf O num = extremosup Entonces
			
			es_igual <- verdadero;
			
		FinSi
		
		media <- media + num;
		
		n <- n + 1;
		
		Si num < extremoinf O num > extremosup Entonces
			
			i <- i + 1;
			
		FinSi
		
	Hasta Que num < 0
	
	Escribir "";
	
	Escribir "La cantidad de n�meros introducidos que no pertenecen al intervalo ser�a de ", i - 1 , ".";
	
	Escribir "La media de los n�meros introducidos es de ", media/n , ".";
	
	Si es_igual Entonces
		
		Escribir "S� se ha introducido un n�mero igual a alguno de los intervalos.";
		
	SiNo
		
		Escribir "No se ha introducido un n�mero igual a alguno de los intervalos.";
		
	FinSi
	
FinProceso
