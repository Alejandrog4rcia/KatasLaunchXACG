# Ejercicio 1
def leer_tanques(main_tank,external_tank,hydrogen_tank):
    return f"""Fuel Report:
    Total Average: {average([main_tank, external_tank, hydrogen_tank])}%
    Main tank: {main_tank}%
    External tank: {external_tank}%
    Hydrogen tank: {hydrogen_tank}% 
    """
def average(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

print(leer_tanques(88, 76, 70))

#Ejercicio 2

def mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report

print(mission_report("Moon", 8, 11, 55, main=300000, external=200000))

