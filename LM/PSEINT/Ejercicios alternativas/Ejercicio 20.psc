
Proceso Ejercicio_20
	
	Definir peso,precio,pais como Real;
	
	Escribir Sin Saltar "Peso de equipaje(en kg): ";
	
	Leer peso;
	
	Escribir "Elija su destino(Marque del 1 al 5):";
	
	Escribir "1) AM�RICA DEL NORTE";
	
	Escribir "2) AM�RICA CENTRAL";
	
	Escribir "3) AM�RICA DEL SUR";
	
	Escribir "4) EUROPA";
	
	Escribir "5) ASIA";
	
	Leer pais;
	
	Si peso > 5 Entonces
		
		Escribir "Se ha rechazado la entrega del paquete por motivos de seguridad";
		
	SiNo
		
		Segun pais Hacer
			
			1:
				
				precio <- peso * 24;
				
				Escribir "La entrega a Am�rica del Norte tendr� un costo de ", precio , " euros.";
				
			2:
				
				precio <- peso * 20;
				
				Escribir "La entrega a Am�rica Central tendr� un costo de ", precio , " euros.";
				
			3:
				
				precio <- peso * 21;
				
				Escribir "La entrega a Am�rica del Sur tendr� un costo de ", precio , " euros.";
				
			4:
				
				precio <- peso * 10;
				
				Escribir "La entrega a Europa tendr� un costo de ", precio , " euros.";
				
			De Otro Modo:
				
				precio <- peso * 18;
				
				Escribir "La entrega a Asia tendr� un costo de ", precio , " euros.";
				
		FinSegun
		
	FinSi
	
FinProceso
