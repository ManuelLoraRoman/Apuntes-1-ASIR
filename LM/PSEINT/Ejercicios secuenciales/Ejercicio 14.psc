
Proceso Ejercicio_14
	
	Definir num,numinv como Real;
	
	Definir numtxt,cad1,cad2 como Cadena;
	
	Escribir Sin Saltar "Escriba el n�mero deseado:";
	
	Leer num;
	
	numtxt <- ConvertirATexto(num);
	
	Si Longitud(numtxt) = 2 Entonces
		
		cad1 <- Subcadena(numtxt,0,0);
		
		cad2 <- Subcadena(numtxt,1,1);
		
		Escribir "El n�mero invertido ser�a: ", Concatenar(cad2,cad1), ".";
		
	SiNo
		
		Escribir "�ERROR! El n�mero introducido no tiene 2 cifras, por favor reinicie el programa. Gracias.";
		
	FinSi

FinProceso
