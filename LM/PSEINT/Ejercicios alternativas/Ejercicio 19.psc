
Proceso Ejercicio_19
	
	Definir num como Real;
	
	Escribir Sin Saltar "Escriba un nº del 1 al 12: ";
	
	Leer num;
	
	Repetir
		
		Si num <=0 O num > 12 Entonces
			
			Escribir "¡ERROR! El número introducido es incorrecto.";
			
			Escribir Sin Saltar "Escriba un nº del 1 al 12: ";
			
			Leer num;
			
		FinSi
		
	Hasta que num >=1 Y num <= 12
	
	Si num = 1 Entonces
		
		Escribir "El mes referido es Enero y tiene 31 días.";
		
	SiNo
		
		Si num = 2 Entonces
			
			Escribir "El mes referido es Febrero y tiene 28 días.";
			
		SiNo
			
			Si num = 3 Entonces
				
				Escribir "El mes referido es Marzo y tiene 31 días.";
				
			SiNo
				
				Si num = 4 Entonces
					
					Escribir "El mes referido es Abril y tiene 30 días.";
					
				SiNo
					
					Si num = 5 Entonces
						
						Escribir "El mes referido es Mayo y tiene 31 días.";
						
					SiNo
						
						Si num = 6 Entonces
							
							Escribir "El mes referido es Junio y tiene 30 días.";
							
						SiNo
							
							Si num = 7 Entonces
								
								Escribir "El mes referido es Julio y tiene 31 días.";
								
							SiNo
								
								Si num = 8 Entonces
									
									Escribir "El mes referido es Agosto y tiene 31 días.";
									
								SiNo
									
									Si num = 9 Entonces
										
										Escribir "El mes referido es Septiembre y tiene 30 días.";
										
									SiNo
										
										Si num = 10 Entonces
											
											Escribir "El mes referido es Octubre y tiene 31 días.";
											
										SiNo
											
											Si num = 11 Entonces
												
												Escribir "El mes referido es Noviembre y tiene 30 días.";
												
											SiNo
												
												Escribir "El mes referido es Diciembre y tiene 31 días.";
												
											FinSi
											
											
										FinSi
										
									FinSi
									
								FinSi
								
							FinSi
							
						FinSi
						
					FinSi
					
				FinSi
				
			FinSi
			
		FinSi
		
		
	FinSi
	
FinProceso
