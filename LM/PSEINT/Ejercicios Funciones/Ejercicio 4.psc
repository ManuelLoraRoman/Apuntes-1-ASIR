

//Crea un funci�n "ConvertirEspaciado", que reciba como par�metro un texto y devuelve una cadena con un espacio adicional tras cada letra.
//Por ejemplo, "Hola, t�" devolver� "H o l a , t � ". Crea un programa principal donde se use dicha funci�n.

Funcion cad <- ConvertirEspaciado(txt)
	
	Definir i como Entero;
	
	i <- 0;
	
	Repetir
		
		Escribir Sin Saltar SubCadena(txt,i,i) , " ";
		
		i <- i + 1;
		
	Hasta Que i = Longitud(txt)
	
FinFuncion

Proceso Espaciar
	
	Definir caden,caden1 como Cadena;
	
	Escribir Sin Saltar "Escriba una cadena: ";
	
	Leer caden;
	
	caden1 <- ConvertirEspaciado(caden);
	
	Escribir caden1;
	
FinProceso
