

Funcion cad <- EsMultiplo(num1,num2)
	
	Si num1 mod num2 = 0 Entonces
		
		Escribir "El ", num1, " es múltiplo de ",num2, ".";
		
	SiNo
		
		Si num2 mod num1 = 0 Entonces
			
			Escribir "El ", num2, " es múltiplo de ",num1, ".";
			
		SiNo
			
			Escribir "No son múltiplos entre ellos";
			
		FinSi
		
	FinSi
	
FinFuncion


Proceso multiplo
	
	Definir numero1,numero2 como Real;
	
	Definir mult como Cadena;
	
	Escribir Sin Saltar "Dime el Primer número: ";
	
	Leer numero1;
	
	Escribir Sin Saltar "Dime el Segundo número: ";
	
	Leer numero2;
	
	mult <- EsMultiplo(numero1,numero2);
	
	Escribir "";
	
FinProceso
