
Proceso Ejercicio_10
	
	Definir x1,y1,x2,y2,r1,r2,dist como Real;
	
	Escribir "Escriba la coordenada x1: ";
	
	Leer x1;
	
	Escribir "Escriba la coordenada y1: ";
	
	Leer y1;
	
	Escribir "Escriba la coordenada x2: ";
	
	Leer x2;
	
	Escribir "Escriba la coordenada y2: ";
	
	Leer y2;
	
	Escribir "Escriba el radio del PTO 1: ";
	
	Leer r1;
	
	Escribir "Escriba el radio del PTO 2: ";
	
	Leer r2;
	
	dist <- abs(x2 - x1);
	
	Si dist > (r1 + r2) Entonces
		
		Escribir "Las circunferencias son exteriores.";
		
	SiNo
		
		Si dist = (r1 + r2) Entonces
			
			Escribir "Las circunferencias son tangentes exteriores.";
			
		SiNo
			
			Si dist < (r1 + r2) Y dist > abs(r1 - r2) Entonces
				
				Escribir "Las circunferencias son secantes.";
				
			SiNo
				
				Si dist = abs(r1 - r2) Entonces
					
					Escribir "Las circunferencias son tangentes interiores.";
					
				SiNo
					
					Si dist > 0 Y dist < abs(r1 - r2) Entonces
						
						Escribir "Las circunferencias son interiores.";
						
					SiNo
						
						Si dist = 0 Entonces
							
							Escribir "Las circunferencias son concéntricas.";
							
							
						FinSi
						
					FinSi
					
					
				FinSi
				
			FinSi
			
		FinSi
		
		
		
		
		
		
	FinSi
	
FinProceso
