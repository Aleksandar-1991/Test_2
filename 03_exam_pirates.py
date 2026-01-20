cities = dict()

while (input_line := input()) != 'Sail':
    tokens = input_line.split('||')
    city, population, gold = tokens[0], int(tokens[1]), int(tokens[2])
    if city not in cities.keys():
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += population
    cities[city]['gold'] += gold

while (input_events := input()) != 'End':
    tokens = input_events.split('=>')
    command = tokens[0]
    if command == 'Plunder':
        town, people, gold_plundered = tokens[1], int(tokens[2]), int(tokens[3])
        print(f"{town} plundered! {gold_plundered} gold stolen, {people} citizens killed.")
        cities[town]['gold'] -= gold_plundered
        cities[town]['population'] -= people
        if cities[town]['gold'] == 0 or cities[town]['population'] == 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]
    elif command == 'Prosper':
        town, additional_gold = tokens[1], int(tokens[2])
        if additional_gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        cities[town]['gold'] += additional_gold
        print(f"{additional_gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
if len(cities.keys()) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
    for tw in cities.keys():
        print(f"{tw} -> Population: {cities[tw]['population']} citizens, Gold: {cities[tw]['gold']} kg")


