
Proceso Ejercicio_2
	
	// Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado. 
	// Copia los elementos del vector en otro vector pero en orden inverso, y muéstralo por la pantalla.
	
	Definir vector_caracteres,vector_inverso,cad Como Cadena;
	
	Definir i como Entero;
	
	Escribir Sin Saltar "Escriba una cadena de 5 caracteres: ";
	
	Leer cad;
	
	Dimension vector_caracteres[5];
	
	Dimension vector_inverso[5];
	
	Para i <- 0 Hasta 4 Hacer
		
		vector_caracteres[i] <- Subcadena(cad,i,i);
		
	FinPara
	
	Para i <- 0 Hasta 4 Hacer
		
		vector_inverso[i] <- vector_caracteres[4 - i];
		
	FinPara
	
	Escribir sin saltar "El vector inverso sería: ";
	
	Para i <- 0 Hasta 4 Hacer
		
		Escribir sin saltar  vector_inverso[i];
		
	FinPara
	
FinProceso
