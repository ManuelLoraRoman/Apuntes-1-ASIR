
#Dadas dos variables numéricas A y B, que el usuario debe teclear,
#se pide realizar un algoritmo que intercambie los valores de ambas variables
#y muestre cuanto valen al final las dos variables.

A = int(input("Dime un número:"))
B = int(input("Dime otro número:"))

C = B
B = A
A = C

print ("Los valores se han intercambiado --> Nº 1 =",A,"y Nº2 =",B,".")
