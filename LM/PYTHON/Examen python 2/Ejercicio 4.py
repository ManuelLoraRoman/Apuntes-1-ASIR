
almacen = []
articulo = []
codigo = 1
nombre = ""
cantidad = 0
precio = 0.0
while codigo != 0:
    codigo = int(input("Introduzca el código del artículo: "))
    if codigo == 0:
        break;
    nombre = str(input("Introduzca el nombre del artículo: "))
    cantidad = int(input("Cantidad del artículo: "))
    precio = float(input("Precio del artículo: "))
    articulo = [codigo,nombre,cantidad,precio]
    almacen.append(articulo)
print("La lista del almacén:",almacen)
print("CODIGO-NOMBRE-PRECIO")
for lista in almacen:
    print("Código:",lista[0],"\nNombre:",lista[1],"\nPrecio con IVA:",int(lista[3]) * 1.21,".")
print("CODIGO-NOMBRE-CANTIDADD < 10")
for lista in almacen:
    if int(lista[2]) < 10:
        print("Código:",lista[0],"\nNombre:",lista[1],".")
cadena = int(input("Introduzca un código: "))
for i in lista:
    if int(lista[0]) == cadena:
        print("Nombre del artículo buscado:",lista[1],".")
