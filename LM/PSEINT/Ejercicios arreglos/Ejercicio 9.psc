
Proceso Ejercicio_9
	
	//Queremos guardar la temperatura m�nima y m�xima de 5 d�as. realiza un programa que de la siguiente informaci�n:
	
    //La temperatura media de cada d�a
    //Los d�as con menos temperatura
    //Se lee una temperatura por teclado y se muestran los d�as cuya temperatura m�xima coincide con ella. si no existe ning�n d�a se muestra un mensaje de informaci�n.
	
	Definir vectortempmin,vectortempmax,vectormediatemp,tempmin,tempmax,temp,i Como Real;
	
	Definir vectordia,dia como Cadena;
	
	Dimension vectortempmin[5],vectortempmax[5],vectordia[5],vectormediatemp[5];
	
	Para i <- 0 Hasta 4 Hacer
		
		Escribir Sin Saltar "Escribe el d�a: ";
		
		Leer dia;
		
		vectordia[i] <- dia;
		
		Escribir Sin Saltar "Escribe la Temp.m�nima de ese d�a: ";
		
		Leer tempmin;
		
		vectortempmin[i] <- tempmin;
		
		Escribir Sin Saltar "Escribe la Temp.m�xima de ese d�a: ";
		
		Leer tempmax;
		
		vectortempmax[i] <- tempmax;
		
		vectormediatemp[i] <- (tempmin + tempmax)/2;
		
	FinPara
	
	i <- 0;
	
	Para i <- 0 Hasta 4 Hacer
		
		Escribir "Media de las temperaturas:";
		
		Escribir vectormediatemp[i];
		
	FinPara
	
	i <- 0;
	
	Escribir Sin Saltar "El d�a con menos temperatura fue: ";
	
	Si vectortempmin[i] < vectortempmin[i + 1] && vectortempmin[i] < vectortempmin[i + 2] && vectortempmin[i] < vectortempmin[i + 3] && vectortempmin[i] < vectortempmin[i + 4]Entonces
		
		Escribir vectortempmin[i];
		
	SiNo
		
		Si vectortempmin[i + 1] < vectortempmin[i] && vectortempmin[i + 1] < vectortempmin[i + 2] && vectortempmin[i + 1] < vectortempmin[i + 3] && vectortempmin[i + 1] < vectortempmin[i + 4]Entonces
			
			Escribir vectortempmin[i + 1];
			
		SiNo
			
			Si vectortempmin[i + 2] < vectortempmin[i] && vectortempmin[i + 2] < vectortempmin[i + 1] && vectortempmin[i + 2] < vectortempmin[i + 3] && vectortempmin[i + 2] < vectortempmin[i + 4]Entonces
				
				Escribir vectortempmin[i + 2];
				
			SiNo
				
				Si vectortempmin[i + 3] < vectortempmin[i] && vectortempmin[i + 3] < vectortempmin[i + 2] && vectortempmin[i + 3] < vectortempmin[i + 1] && vectortempmin[i + 3] < vectortempmin[i + 4]Entonces
					
					Escribir vectortempmin[i + 3];
					
				SiNo
					
					Escribir vectortempmin[i + 4];
					
				FinSi
				
				
			FinSi
			
			
		FinSi
		
		
	FinSi
	
	Escribir Sin Saltar "Escribe una temperatura: ";
	
	Leer temp;
	
	Para i <- 0 Hasta 4 Hacer
		
		Si tempmax = vectortempmax[i] Entonces
			
			Segun i Hacer
				
				0:
					
					Escribir vectordia[0];
					
				1:
					
					Escribir vectordia[1];
					
				2:
					
					Escribir vectordia[2];
					
				3:
					
					Escribir vectordia[3];
					
				De Otro Modo:
					
					Escribir vectordia[4];
					
			FinSegun
			
		SiNo
			
			Escribir "No hay ninguna temperatura que corresponda a la dada.";
			
		FinSi
		
	FinPara
	
FinProceso
