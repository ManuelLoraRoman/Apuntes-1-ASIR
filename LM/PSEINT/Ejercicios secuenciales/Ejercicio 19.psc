
Proceso Ejercicio_19
	
	
	Definir numpreg,corr,fallo,blanco,total como Real;
	
	Escribir Sin Saltar "Escribe el n� de preguntas: ";
	
	Leer numpreg;
	
	Escribir Sin Saltar "Escribe el n� de P. correctas: ";
	
	Leer corr;
	
	Escribir Sin Saltar "Escribe el n� de P. err�neas: ";
	
	Leer fallo;
	
	Escribir Sin Saltar "Escribe el n� de P. en blanco: ";
	
	Leer blanco;
	
	total <- ((corr * 5)+(fallo * (-1)));
	
	Escribir "El puntuaje total ser�a de ", total, " de puntos.";
	
	
	
FinProceso
