
#La letra del DNI se calcula a partir de su número. Para ello se divide el número entre 23 y el resto
#(que tiene que ser un número entre 0 y 22 se sustituye por la letra correspondiente de la siguiente tabla:

 #0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
 #T R W A G M Y F P D X  B  N  J  Z  S  Q  V  H  L  C  K  E

#Escribe un programa que te pida un número de DNI y una letra y te diga si es correcto o no.

diccionario = {'T':0,'R':1,'W':2,'A':3,'G':4,'M':5,'Y':6,'F':7,'P':8,'D':9,'X':10,'B':11,'N':12,'J':13,'Z':14,'S':15,'Q':16,'V':17,'H':18,'L':19,'C':20,'K':21,'E':22}
num = int(input("Dame un número de DNI: "))
letra = str(input("Dame la letra del DNI: "))
print("DNI:",num,"-",letra)
resto = round(num % 23)
if diccionario[letra.upper()] == resto:
    print("Es correcto el DNI.")
else:
    print("No es correcto el DNI.")
