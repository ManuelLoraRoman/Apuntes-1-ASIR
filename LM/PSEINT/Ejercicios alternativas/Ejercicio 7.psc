
Proceso Ejercicio_7
	
	Definir base,expo como Real;
	
	Escribir Sin Saltar "Escriba la base de su potencia: ";
	
	Leer base;
	
	Escribir Sin Saltar "Escriba el exponente de su potencia: ";
	
	Leer expo;
	
	Si expo > 0 Entonces
		
		Escribir "La potencia ser�a: ",base," ^ ",expo," y su soluci�n es ", base ^ expo , ".";
		
	SiNo
		
		Si expo = 0 Entonces
			
			Escribir "La potencia ser�a: ",base," ^ ",expo," y su soluci�n es ", base ^ expo , ".";
			
		SiNo
			
			Escribir "La potencia ser�a: ",base," ^ ",expo," y su soluci�n es ", (base ^ expo), ".";
			
		FinSi
	FinSi
	
FinProceso
