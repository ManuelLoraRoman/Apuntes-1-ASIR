
print("CONVERTIDOR DE CM A KM, M Y CM")
dist = int(input("Escriba una distancia en centímetros: "))
print(dist,"centímetros son ",end="")

distkm = dist // 100000
distm = (dist % 100000) // 100
distcm = (dist % 100000) % 100

print(distkm,"km,",distm,"m y",distcm,"cm.")
