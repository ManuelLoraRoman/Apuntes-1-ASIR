
Proceso Ejercicio_12
	
	Definir x1,x2,y1,y2,distancia como Real;
	
	Escribir Sin Saltar "Escriba la coordenada x del punto A: ";
	
	Leer x1;
	
	Escribir Sin Saltar "Escriba la coordenada y del punto A: ";
	
	Leer y2;
	
	Escribir "El punto A es (",x1, ",", y2 ,")." ;
	
	Escribir Sin Saltar "Escriba la coordenada x del punto B: ";
	
	Leer x2;
	
	Escribir Sin Saltar "Escriba la coordenada y del punto B: ";
	
	Leer y1;
	
	Escribir "El punto B es (",x2, ",", y1 ,")." ;
	
	distancia <- rc((x2 - x1)^2 + (y2 - y1)^2);
	
	Escribir "La distancia entre los dos puntos es: ", distancia, " cm.";
	
FinProceso
