#Ejercicio 1
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets += ['Pluton']
num_planets = len(planets)
print ("Hay un total de " + str(num_planets) + " planetas, El ultimo agregado es:", planets[8])
#Ejercicio 2
planets2 = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
user_planet=input("Introduzca el nombre del planeta comenzando con la primera letra en mayuscula: ")
planet_index = planets2.index(user_planet)
print(planet_index)
print('Estos son los planetas que estan mas cerca del sol en comparacion a  ' + user_planet)
print(planets2[0:planet_index])
print('Estos son los planetas que estan mas alejados del sol en comparacion a ' + user_planet)
print(planets2[planet_index + 1:])

