
Proceso Ejercicio_1
	
	Definir intensidad,resis1,resis2,resisequiv,voltaje como Real;
	
	Escribir Sin Saltar "Escribe la intensidad que recorre el circuito: ";
	
	Leer intensidad;
	
	Escribir Sin Saltar "Escribe la resistencia n�1: ";
	
	Leer resis1;
	
	Escribir Sin Saltar "Escribe ahora la resistencia n�2: ";
	
	Leer resis2;
	
	Escribir "";
	
	Escribir "Para un circuito en serie: ";
	
	resisequiv <- resis1 + resis2;
	
	voltaje <- intensidad * resisequiv;
	
	Escribir "La resistencia equivalente ser�a ", resisequiv , " y el voltaje de la fuente de alimentaci�n ser�a ", voltaje , ".";
	
	Escribir "";
	
	voltaje <- 0;
	
	resisequiv <- 0;
	
	Escribir "Para un circuito en paralelo: ";
	
	resisequiv <- 1 /((1/resis1)+(1/resis2));
	
	voltaje <- intensidad * resisequiv;
	
	Escribir "La resistencia equivalente ser�a ", resisequiv , " y el voltaje de la fuente de alimentaci�n ser�a ", voltaje , ".";
	
	Escribir "";
	
FinProceso
