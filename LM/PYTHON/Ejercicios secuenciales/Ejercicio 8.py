
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
#y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

venta1 = int(input("Venta nº1(en euros €):"))
venta2 = int(input("Venta nº2(en euros €):"))
venta3 = int(input("Venta nº3(en euros €):"))
ventatotal = venta1 + venta2 + venta3
comisiontotal = (venta1 / 10) + (venta2 / 10) + (venta3 / 10)

print("La comisión total sería:",comisiontotal,".")
print("El total que recibirá en el mes(en euros €) será de:", ventatotal + comisiontotal)
