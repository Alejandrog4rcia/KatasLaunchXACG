from datetime import date
sum = 1 + 2
product = sum * 2
print(product)

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

print("Today's date is: " + str(date.today()))

print("Buen día")
name = input("Tu nombre: ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))