
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

num1 = int(input("Dime un número:"))
num2 = int(input("Dime otro número:"))
num3 = int(input("Dime el último número:"))

if num1 > num2 and num1 > num3:
	pos1 = num1
    if num2 > num3:
        pos2 = num2
        pos3 = num3
        print("El orden de mayor a menor sería:",pos1,">",pos2,">",pos3,".")
    else:
        pos2 = num3
		pos3 = num2
		print("El orden de mayor a menor sería:",pos1,">",pos2,">",pos3,".")

if num2 > num1 and num2 > num3:
	pos1 = num2
	if num1 > num3:
        pos2 = num1
        pos3 = num3
        print("El orden de mayor a menor sería:",pos1,">",pos2,">",pos3,".")
    else:
        pos2 = num3
        pos3 = num1
        print("El orden de mayor a menor sería:",pos1,">",pos2,">",pos3,".")

if num3 > num1 and num3 > num2:
	pos1 = num3
	if num1 > num2:
        pos2 = num1
        pos3 = num2
        print("El orden de mayor a menor sería:",pos1,">",pos2,">",pos3,".")
    else:
        pos2 = num2
        pos3 = num1
        print("El orden de mayor a menor sería:",pos1 ,">",pos2,">",pos3,".")
