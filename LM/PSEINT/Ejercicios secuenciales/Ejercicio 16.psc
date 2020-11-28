
Proceso Ejercicio_16
	
	Definir v1,v2,d,tiempo_enc como Real;
	
	Escribir "Escribe a que distancia se encuentran los dos vehículos (km):";
	
	Leer d;
	
	Repetir
		
		Escribir "Escribe la velocidad del coche 1(delante):";
		
		Leer v1;
		
		Escribir "Escribe la velocidad del coche 2(detrás):";
		
		Leer v2;
		
		Si v2 < v1 Entonces
			
			Escribir "La velocidad del 2º coche debe ser mayor que la del 1er coche.";
			
		FinSi
		
	Hasta Que v2 > v1
	
	tiempo_enc <- d / (v2 - v1);
	
	Escribir "El coche 2 alcanzará al coche 1 en ", redon(tiempo_enc * 60) , " minutos.";
	
FinProceso
