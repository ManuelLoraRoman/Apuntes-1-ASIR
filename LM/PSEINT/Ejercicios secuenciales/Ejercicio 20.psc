
Proceso Ejercicio_20
	
	Definir numnum,n,cant,i como Real;
	
	Definir es_primo como Logico;
	
	Escribir Sin Saltar "Escribe la cantidad de números primos a mostrar: ";
	
	Leer numnum;
	
	Escribir "1: 2";
	
	cant <- 1;
	
	n <- 3;
	
	Mientras cant < numnum Hacer
		
		es_primo <- Verdadero;
		
		Para i <- 3 Hasta rc(n) Con Paso 2 Hacer
			
			Si n MOD i = 0 Entonces
				
				es_primo <- Falso;
				
			FinSi
			
		FinPara
		
		Si es_primo Entonces
			
			cant <- cant + 1;
			
			Escribir cant, ": " , n;
			
		FinSi
		
		n <- n + 2;
		
	FinMientras
	
FinProceso
