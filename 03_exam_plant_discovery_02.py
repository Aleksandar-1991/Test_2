n = int(input())

plants = dict()
for i in range(n):
    user_input = input().split("<->")
    plant_name, rarity = user_input[0], int(user_input[1])
    if plant_name not in plants.keys():
        plants[plant_name] = {'rarity': int(), 'rating': list() }
    plants[plant_name]['rarity'] = rarity

while (tokens := input()) != 'Exhibition':
    splitted_input = tokens.split(': ')
    command = splitted_input[0]
    if command == 'Rate':
        input_second_half = splitted_input[1].split(' - ')
        plant, rating = input_second_half[0], float(input_second_half[1])
        if plant not in plants.keys():
            print("error")
            continue
        plants[plant]['rating'].append(rating)
    elif command == 'Update':
        input_second_half = splitted_input[1].split(' - ')
        plant, new_rarity = input_second_half[0], int(input_second_half[1])
        if plant not in plants.keys():
            print("error")
            continue
        plants[plant]['rarity'] = new_rarity
    elif command == 'Reset':
        plant = splitted_input[1]
        if plant not in plants.keys():
            print("error")
            continue
        plants[plant]['rating'] = list()

print("Plants for the exhibition:")
for pl in plants:
    if plants[pl]['rating']:
        average_rating = sum(plants[pl]['rating'])/len(plants[pl]['rating'])
    else:
        average_rating = 0
    print(f"- {pl}; Rarity: {plants[pl]['rarity']}; Rating: {average_rating:.2f}")

