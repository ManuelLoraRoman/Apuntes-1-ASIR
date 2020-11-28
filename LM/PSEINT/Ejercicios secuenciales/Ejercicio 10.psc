
Proceso Ejercicio_10
	
	Definir cal1,cal2,cal3,exa,trab,porc1,porc2,porc3,total como Real;
	
	Escribir Sin Saltar "Calificación primer parcial: ";
	
	Leer cal1;
	
	Escribir Sin Saltar "Calificación segundo parcial: ";
	
	Leer cal2;
	
	Escribir Sin Saltar "Calificación tercer parcial: ";
	
	Leer cal3;
	
	Escribir Sin Saltar "Calificación examen final: ";
	
	Leer exa;
	
	Escribir Sin Saltar "Calificación trabajo final: ";
	
	Leer trab;
	
	porc1 <- (((cal1 + cal2 + cal3) / 3) * 0.55);
	
	porc2 <- 0.3 * exa;
	
	porc3 <- 0.12 * trab;
	
	total <- porc1 + porc2 + porc3;
	
	Escribir "La calificación final en la materia de Algoritmos es ", total, ".";
	
FinProceso
