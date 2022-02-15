#Ejercicio1
distplaneta=149597870
distplanetb=778547200
distkm=distplanetb-distplaneta
print( str(distkm) + ' km')
print( str(round(distkm * 0.621)) + ' mi')
#Ejercicio2
distplaneta = int(input("¿Cuál es la distancia del primer planeta? "))
distplanetb = int(input("¿Cuál es la distancia del segundo planeta? "))
dist_km= distplanetb - distplaneta
print(dist_km)
distmi = dist_km * 0.621
print(abs(distmi))