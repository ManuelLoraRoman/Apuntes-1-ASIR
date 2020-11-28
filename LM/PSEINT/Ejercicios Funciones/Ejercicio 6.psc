
//Dise�ar una funci�n que calcule el �rea y el per�metro de una circunferencia. 
//Utiliza dicha funci�n en un programa principal que lea el radio de una circunferencia y muestre su �rea y per�metro.

Funcion calc <- calculoArea(radiocircunferencia)
	
	Definir calc como Real;
	
	calc <- (radiocircunferencia ^ 2) * PI;
	
FinFuncion

Funcion calcu <- calculoPerimetro(radiocircunferencia)
	
	Definir calcu como Real;
	
	calcu <- (2 * radiocircunferencia) * PI; 
	
FinFuncion


Proceso Ejercicio_6
	
	Definir area,perimetro,radio como Real;
	
	Escribir Sin Saltar "Escriba el radio que desee de una circunferencia: ";
	
	Leer radio;
	
	area <- calculoArea(radio);
	
	perimetro <- calculoPerimetro(radio);
	
	Escribir "El �rea deseada ser�: " , area , ".";
	
	Escribir "El per�metro deseado ser�: ", perimetro , ".";
	
FinProceso
