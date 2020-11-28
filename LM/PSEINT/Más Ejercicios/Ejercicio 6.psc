
Proceso Ejercicio_6
	
	//Crear un programa que convierta un número entero 
	//(mayor que 1 y menor o igual que 1000) a número romano.
	
	Definir num,i como Entero;
	
	Definir numtxt,romano como Cadena;
	
	Escribir Sin Saltar "Escriba un número para convertirlo a romano: ";
	
	Leer num;
	
	numtxt <- ConvertirATexto(num);
	
	Si Longitud(numtxt) = 4 Entonces
		
		romano <- "M";
		
		Escribir "El número convertido a romano sería: ", romano , ".";
		
	SiNo
		
		Si Longitud(numtxt) = 1 Entonces
			
			Segun num Hacer
				1:
					
					romano <- "I";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				2:
					
					romano <- "II";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				3:
					
					romano <- "III";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				4:
					
					romano <- "IV";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				5:
					
					romano <- "V";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				6:
					
					romano <- "VI";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				7:
					
					romano <- "VII";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				8:
					
					romano <- "VIII";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
				De Otro Modo:
					
					romano <- "IX";
					
					Escribir "El número convertido a romano sería: ", romano , ".";
					
			FinSegun
			
		SiNo
			
			Si Longitud(numtxt) = 2 Entonces
				
				Segun ConvertirANumero(Subcadena(numtxt,0,0)) Hacer
					
					1:
						
						romano <- "X";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					2:
						
						romano <- "XX";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					3:
						
						romano <- "XXX";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					4:
						
						romano <- "XL";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					5:
						
						romano <- "L";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					6:
						
						romano <- "LX";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					7:
						
						romano <- "LXX";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					8:
						
						romano <- "LXXX";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
					De Otro Modo:
						
						romano <- "XC";
						
						Escribir "El número convertido a romano sería: ", romano , ".";
						
				FinSegun
				
				
				
			FinSi
			
		FinSi
		
	FinSi
	
	
FinProceso
