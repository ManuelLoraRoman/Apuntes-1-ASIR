
Proceso Ejercicio_17
	
	Definir HH,MM,SS,T,seginicial,total,horallegada,minllegada,segllegada Como Entero;
	
	Escribir "A continuación, escribirá la hora de salida del ciclista.";
	
	Escribir Sin Saltar "Escribir las horas:";
	
	Leer HH;
	
	Escribir Sin Saltar "Escribir las minutos:";
	
	Leer MM;
	
	Escribir Sin Saltar "Escribir los segundos";
	
	Leer SS;
	
	Escribir Sin Saltar "Ya definida la hora de salida, indique cuanto tarda en llegar al punto de destino(en segundos):";
	
	Leer T;
	
	seginicial <- HH * 3600 + MM * 60 + SS;
	
	total <- seginicial + T;
	
	horallegada <- trunc(total / 3600);
	
	minllegada <- trunc((total % 3600) / 60);
	
	segllegada <- (total % 3600) % 60;
	
	Escribir "La hora de llegada será: ", horallegada,":",minllegada,":",segllegada;
	
FinProceso
