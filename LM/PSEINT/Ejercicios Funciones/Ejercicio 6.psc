
//Diseñar una función que calcule el área y el perímetro de una circunferencia. 
//Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

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
	
	Escribir "El área deseada será: " , area , ".";
	
	Escribir "El perímetro deseado será: ", perimetro , ".";
	
FinProceso
