
Proceso Ejercicio_5
	
	Definir carac como Cadena;
	
	Repetir
		
		Escribir Sin Saltar "Escriba un carácter: ";
		
		Leer carac;
		
		Si carac = "a" o carac = "A" o carac = "e" o carac = "E" o carac = "i" o carac = "I" o carac = "o" o carac = "O" o carac = "u" o carac = "U" Entonces
			
			Escribir "ES VOCAL";
			
		SiNo
			
			Si carac = " " Entonces
				
				Escribir "FIN DE PROGRAMA";
				
			SiNo
				
				Escribir "NO ES VOCAL";
				
			FinSi
			
		FinSi
		
	Hasta Que carac = " "
	
FinProceso
