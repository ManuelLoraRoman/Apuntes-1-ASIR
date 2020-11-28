

//Crea un función "ConvertirEspaciado", que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
//Por ejemplo, "Hola, tú" devolverá "H o l a , t ú ". Crea un programa principal donde se use dicha función.

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
