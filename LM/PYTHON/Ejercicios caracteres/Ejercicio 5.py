
#Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.
import re

cadena = str(input("Dame un nombre y apellidos: "))
m = re.findall('([A-Z])[A-Za-z]* *',cadena)
inic = "".join(m)
print(inic)
