
Proceso Ejercicio_8
	
	Definir sbase,comision,venta1,venta2,venta3,total como Real;
	
	Escribir Sin Saltar "Sueldo Base: ";
	
	Leer sbase;
	
	Escribir Sin Saltar "Venta nº1: ";
	
	Leer venta1;
	
	Escribir Sin Saltar "Venta nº2: ";
	
	Leer venta2;
	
	Escribir Sin Saltar "Venta nº3: ";
	
	Leer venta3;
	
	comision <- (0.1 * venta1) + (0.1 * venta2) + (0.1 * venta3);
	
	total <- sbase + comision;
	
	Escribir "La comisión total por las ventas sería ", comision, ".";
	
	Escribir "El total de sueldo base más comisiones sería ", total, ".";
	
FinProceso
