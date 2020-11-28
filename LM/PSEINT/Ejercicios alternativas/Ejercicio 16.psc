
Proceso Ejercicio_16
	
	Definir temp,precio como Real;
	
	Definir dia,turno como Cadena;
	
	Escribir Sin Saltar "Duración de la llamada: ";
	
	Leer temp;
	
	Escribir Sin Saltar "Día de la semana: ";
	
	Leer dia;
	
	Escribir Sin Saltar "¿Es por la mañana o por la tarde?: ";
	
	Leer turno;
	
	Segun temp Hacer
		
		1,2,3,4,5:
			
			Si dia = "Domingo" O dia = "domingo" Entonces
				
				Escribir "Debes pagar en concepto de llamada: " ,1 + (1 * 0.03), " euros.";
				
			SiNo
				
				Si turno = "mañana" O turno = "Mañana" Entonces
					
					Escribir "Debes pagar en concepto de llamada: " ,1 + (1 * 0.15), " euros.";
					
				SiNo
					
					Escribir "Debes pagar en concepto de llamada: " ,1 + (1 * 0.10), " euros.";
					
				FinSi
				
				
			FinSi
			
		6,7,8:
			
			Si dia = "Domingo" O dia = "domingo" Entonces
				
				Escribir "Debes pagar en concepto de llamada: " ,1.8 + (1.8 * 0.03), " euros.";
				
			SiNo
				
				Si turno = "mañana" O turno = "Mañana" Entonces
					
					Escribir "Debes pagar en concepto de llamada: " ,1.8 + (1.8 * 0.15), " euros.";
					
				SiNo
					
					Escribir "Debes pagar en concepto de llamada: " ,1.8 + (1.8 * 0.10), " euros.";
					
				FinSi
				
				
			FinSi
			
			
		9,10:
			
			Si dia = "Domingo" O dia = "domingo" Entonces
				
				Escribir "Debes pagar en concepto de llamada: " , 2.5 + (2.5 * 0.03), " euros.";
				
			SiNo
				
				Si turno = "mañana" O turno = "Mañana" Entonces
					
					Escribir "Debes pagar en concepto de llamada: " ,2.5 + (2.5 * 0.15), " euros.";
					
				SiNo
					
					Escribir "Debes pagar en concepto de llamada: " ,2.5 + (2.5 * 0.10), " euros.";
					
				FinSi
				
				
			FinSi
			
		De Otro Modo:
			
			Si dia = "Domingo" O dia = "domingo" Entonces
				
				Escribir "Debes pagar en concepto de llamada: " ,3 + (3 * 0.03), " euros.";
				
			SiNo
				
				Si turno = "mañana" O turno = "Mañana" Entonces
					
					Escribir "Debes pagar en concepto de llamada: " ,3 + (3 * 0.15), " euros.";
					
				SiNo
					
					Escribir "Debes pagar en concepto de llamada: " ,3 + (3 * 0.10), " euros.";
					
				FinSi
				
				
			FinSi
			
	FinSegun
	
FinProceso
