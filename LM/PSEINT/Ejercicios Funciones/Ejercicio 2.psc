

Funcion cad <- EsMultiplo(num1,num2)
	
	Si num1 mod num2 = 0 Entonces
		
		Escribir "El ", num1, " es m�ltiplo de ",num2, ".";
		
	SiNo
		
		Si num2 mod num1 = 0 Entonces
			
			Escribir "El ", num2, " es m�ltiplo de ",num1, ".";
			
		SiNo
			
			Escribir "No son m�ltiplos entre ellos";
			
		FinSi
		
	FinSi
	
FinFuncion


Proceso multiplo
	
	Definir numero1,numero2 como Real;
	
	Definir mult como Cadena;
	
	Escribir Sin Saltar "Dime el Primer n�mero: ";
	
	Leer numero1;
	
	Escribir Sin Saltar "Dime el Segundo n�mero: ";
	
	Leer numero2;
	
	mult <- EsMultiplo(numero1,numero2);
	
	Escribir "";
	
FinProceso
