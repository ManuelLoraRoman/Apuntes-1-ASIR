
Funcion Leer_numero()
	
	Definir es_negativo como logico;
	
	Definir num Como Entero;
	
	Leer num;
	
	Si num < 0 Entonces
		
		es_negativo <- Verdadero;
		
	FinSi
	
FinFuncion

Funcion EstaDentroIntervalo(limiteinf,limitesup,num)
	
	Definir dentro_intervalo como logico;
	
	Si num < limitesup && num > limiteinf Entonces
		
		dentro_intervalo <- verdadero;
		
	FinSi
	
FinFuncion

Funcion EsUnLimite(limiteinf,limitesup,num)
	
	Definir es_igual como logico;
	
	Si num = limitesup O num = limiteinf Entonces
		
		es_igual <- verdadero;
		
	FinSi
	
FinFuncion



Proceso Ejerciciofunciones_4
	
	Definir extremoinf,extremosup,num,media,i,n como Entero;
	
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
		
		num <- 0;
		
		Escribir Sin Saltar "Escriba un n�mero para su comprobaci�n: ";
		
		Leer_numero();
		
		EsUnLimite(extremoinf,extremosup,num);
		
		media <- media + num;
		
		n <- n + 1;
		
		EstaDentroIntervalo(extremoinf,extremosup,num);
		
	Hasta Que num < 0
	
	Escribir "";
	
	Escribir "La cantidad de n�meros introducidos que no pertenecen al intervalo ser�a de ", i , ".";
	
	Escribir "La media de los n�meros introducidos es de ", media/n , ".";
	
	Si es_igual Entonces
		
		Escribir "S� se ha introducido un n�mero igual a alguno de los intervalos.";
		
	SiNo
		
		Escribir "No se ha introducido un n�mero igual a alguno de los intervalos.";
		
	FinSi
	
FinProceso
