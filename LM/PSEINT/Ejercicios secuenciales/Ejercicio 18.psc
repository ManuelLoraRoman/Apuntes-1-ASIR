
Proceso Ejercicio_18
	
	
	Definir nombre,ape1,ape2,inic como Cadena;
	
	Escribir Sin Saltar "Escriba su nombre: ";
	
	Leer nombre;
	
	Escribir Sin Saltar "Escriba ahora su primer apellido: ";
	
	Leer ape1;
	
	Escribir Sin Saltar "Escriba por último su segundo apellido: ";
	
	Leer ape2;
	
	inic <- Concatenar(SubCadena(nombre,0,0),Subcadena(ape1,0,0));
	
	Escribir "Sus iniciales son: ",Concatenar(inic,Subcadena(ape2,0,0)), ".";
	
	
FinProceso
