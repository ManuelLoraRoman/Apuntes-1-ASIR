
Proceso Ejercicio_6
	
	//Crear un programa que convierta un n�mero entero 
	//(mayor que 1 y menor o igual que 1000) a n�mero romano.
	
	Definir num,i como Entero;
	
	Definir numtxt,romano como Cadena;
	
	Escribir Sin Saltar "Escriba un n�mero para convertirlo a romano: ";
	
	Leer num;
	
	numtxt <- ConvertirATexto(num);
	
	Si Longitud(numtxt) = 4 Entonces
		
		romano <- "M";
		
		Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
		
	SiNo
		
		Si Longitud(numtxt) = 1 Entonces
			
			Segun num Hacer
				1:
					
					romano <- "I";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				2:
					
					romano <- "II";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				3:
					
					romano <- "III";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				4:
					
					romano <- "IV";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				5:
					
					romano <- "V";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				6:
					
					romano <- "VI";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				7:
					
					romano <- "VII";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				8:
					
					romano <- "VIII";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
				De Otro Modo:
					
					romano <- "IX";
					
					Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
					
			FinSegun
			
		SiNo
			
			Si Longitud(numtxt) = 2 Entonces
				
				Segun ConvertirANumero(Subcadena(numtxt,0,0)) Hacer
					
					1:
						
						romano <- "X";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					2:
						
						romano <- "XX";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					3:
						
						romano <- "XXX";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					4:
						
						romano <- "XL";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					5:
						
						romano <- "L";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					6:
						
						romano <- "LX";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					7:
						
						romano <- "LXX";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					8:
						
						romano <- "LXXX";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
					De Otro Modo:
						
						romano <- "XC";
						
						Escribir "El n�mero convertido a romano ser�a: ", romano , ".";
						
				FinSegun
				
				
				
			FinSi
			
		FinSi
		
	FinSi
	
	
FinProceso
