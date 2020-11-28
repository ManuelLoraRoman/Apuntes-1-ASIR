
Proceso Ejercicio_19
	
	Definir button1,button2,button3,button4 como Cadena;
	
	Definir accion como Real;
	
	Definir n como Real;
	
	Escribir "    MENÚ";
	
	Escribir "____________";
	
	Escribir "";
	
	Escribir " _______ ";
	
	Escribir "|       |";
	
	Escribir "|BOTÓN 1|";
	
	Escribir "|_______| ";
	
	Escribir "";
	
	Escribir " _______ ";
	
	Escribir "|       |";
	
	Escribir "|BOTÓN 2|                  (Para salir pulse 0)";
	
	Escribir "|_______| ";
	
	Escribir "";
	
	Escribir " _______ ";
	
	Escribir "|       |";
	
	Escribir "|BOTÓN 3|";
	
	Escribir "|_______| ";
	
	Escribir "";
	
	Escribir " _______ ";
	
	Escribir "|       |";
	
	Escribir "| SALIR |";
	
	Escribir "|_______| ";
	
	Escribir "";
	
	Repetir
		
		Leer accion;
		
		Segun accion Hacer
			
			1:
				
				Definir gradoF,gradoC Como Real;
				
				Escribir "Grado Fahrenheit:";
				
				Leer gradoF;
				
				gradoC <- (gradoF - 32)* (5 / 9);
				
				Escribir "La conversión de grados sería: ", gradoF, " F a ", gradoC, " Cº.";
				
			2:
				
				Definir sbase,comision,venta1,venta2,venta3,total como Real;
				
				Escribir "Sueldo Base:";
				
				Leer sbase;
				
				Escribir "Venta nº1:";
				
				Leer venta1;
				
				Escribir "Venta nº2:";
				
				Leer venta2;
				
				Escribir "Venta nº3:";
				
				Leer venta3;
				
				comision <- (0.1 * venta1) + (0.1 * venta2) + (0.1 * venta3);
				
				total <- sbase + comision;
				
				Escribir "La comisión total por las ventas sería ", comision, ".";
				
				Escribir "El total de sueldo base más comisiones sería ", total, ".";
				
			3:
				
				Definir cal1,cal2,cal3,exa,trab,porc1,porc2,porc3,total como Real;
				
				Escribir "Calificación primer parcial:";
				
				Leer cal1;
				
				Escribir "Calificación segundo parcial:";
				
				Leer cal2;
				
				Escribir "Calificación tercer parcial:";
				
				Leer cal3;
				
				Escribir "Calificación examen final:";
				
				Leer exa;
				
				Escribir "Calificación trabajo final:";
				
				Leer trab;
				
				porc1 <- (((cal1 + cal2 + cal3) / 3) * 0.55);
				
				porc2 <- 0.3 * exa;
				
				porc3 <- 0.12 * trab;
				
				total <- porc1 + porc2 + porc3;
				
				Escribir "La calificación final en la materia de Algoritmos es ", total, ".";
				
			De Otro Modo:
				
				Escribir "    MENÚ";
				
				Escribir "____________";
				
				Escribir "";
				
				Escribir " _______ ";
				
				Escribir "|       |";
				
				Escribir "|BOTÓN 1|";
				
				Escribir "|_______| ";
				
				Escribir "";
				
				Escribir " _______ ";
				
				Escribir "|       |";
				
				Escribir "|BOTÓN 2|";
				
				Escribir "|_______| ";
				
				Escribir "";
				
				Escribir " _______ ";
				
				Escribir "|       |";
				
				Escribir "|BOTÓN 3|";
				
				Escribir "|_______| ";
				
				Escribir "";
				
				Escribir " _______ ";
				
				Escribir "|       |";
				
				Escribir "| SALIR |";
				
				Escribir "|_______| ";
				
				Escribir "";
				
		FinSegun
		
	Hasta Que accion = 0
	
FinProceso
