#Ejercicio 1
new_planet = ''
planets = []
while new_planet.lower() != 'f':
    if new_planet:
        planets.append(new_planet.capitalize())
    new_planet = input('Escribe el planeta o escribe f para terminar ')

#Ejercicio 2
for planet in planets:
    print(planet)
