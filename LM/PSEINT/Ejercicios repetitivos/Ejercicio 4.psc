
Proceso Ejercicio_4
	
	Definir numtxt,long como Cadena;
	
	Definir mayor,menor,igual,n como Real;
	
	Escribir Sin Saltar "Escribe la cantidad de números deseada: ";
	
	Leer numtxt;
	
	mayor <- 0;
	
	menor <- 0;
	
	igual <- 0;
	
	n <- 0;
	
	Repetir
		
		long <- Subcadena(numtxt,n,n);
		
		Si ConvertirANumero(long) > 0 Entonces
			
			mayor <- mayor + 1;
			
		SiNo
			
			Si ConvertirANumero(long) < 0 Entonces
				
				menor <- menor + 1;
				
			SiNo
				
				igual <- igual + 1;
				
			FinSi
			
		FinSi
		
		n <- n + 1;
		
	Hasta Que n = Longitud(numtxt)
	
	Escribir "Hay ", mayor , " nº mayores que 0, " , menor , " nº menores que 0, y ", igual , " iguales a 0.";
	
FinProceso
