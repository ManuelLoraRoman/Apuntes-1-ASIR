
Proceso Ejercicio_19
	
	
	Definir numpreg,corr,fallo,blanco,total como Real;
	
	Escribir Sin Saltar "Escribe el nº de preguntas: ";
	
	Leer numpreg;
	
	Escribir Sin Saltar "Escribe el nº de P. correctas: ";
	
	Leer corr;
	
	Escribir Sin Saltar "Escribe el nº de P. erróneas: ";
	
	Leer fallo;
	
	Escribir Sin Saltar "Escribe el nº de P. en blanco: ";
	
	Leer blanco;
	
	total <- ((corr * 5)+(fallo * (-1)));
	
	Escribir "El puntuaje total sería de ", total, " de puntos.";
	
	
	
FinProceso
