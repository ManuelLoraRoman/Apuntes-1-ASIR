
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
#circunferencias y las clasifique en uno de estos estados:
#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas

x1 = int(input("Coordenada x1:"))
y1 = int(input("Coordenada y1:"))
r1 = int(input("Radio de la Pto 1:"))
print("(",x1,",",y1,")")
print("Radio -->",r1)

x2 = int(input("Coordenada x2:"))
y2 = int(input("Coordenada y2:"))
r2 = int(input("Radio de la Pto 2:"))
print("(",x2,",",y2,")")
print("Radio -->",r2)

dist = abs(x2 - x1)

if dist > (r2 + r1):
    print("Las circunferencias son exteriores.")
else:
    if dist == (r1 + r2):
        print("Las circunferencias son tangentes exteriores.")
    else:
        if dist < (r1 + r2) and dist > abs(r1 - r2):
            print("Las circunferencias son secantes.")
if dist == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores.")
else:
    if dist > 0 and dist < (r1 - r2):
        print("Las circunferencias son interiores.")
    else:
        if dist == 0:
            print("Las circunferencias son concéntricas.")
