
Proceso Ejercicio_8
	
	//Queremos guardar los nombres y la edades de los alumnos de un curso.
	//Realiza un programa que introduzca el nombre y la edad de cada alumno. 
	//El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
	
    //Todos lo alumnos mayores de edad.
    //Los alumnos mayores (los que tienen más edad)
	
	
	Definir vectornombre,nombre como Cadena;
	
	Dimension vectornombre[];
	
	Definir vectoredad,edad,i como Entero;
	
	Dimension vectoredad[];
	
	i <- 0;
	
	Mientras nombre = "*" Hacer
		
		Escribir Sin Saltar "Escriba el nombre de un alumno: ";
		
		Leer nombre;
		
		Escribir Sin Saltar "Escriba la edad de dicho alumno: ";
		
		Leer edad;
		
		vectornombre[i] <- nombre;
		
		
	FinMientras
	
FinProceso
