n = int(input())

plants = dict()
for i in range(n):
    plant, rarity = input().split('<->')
    rarity = float(rarity)
    if plant not in plants.keys():
        plants[plant] = {'rarity': float(), 'rating': []}
    plants[plant]['rarity'] = rarity
while (tokens := input()) != 'Exhibition':
    input_line = tokens.split(': ')
    command = input_line[0]
    if command == 'Rate':
        plant, rating = input_line[1].split(' - ')
        rating = float(rating)
        if plant not in plants:
            print('error')
            continue
        plants[plant]['rating'].append(rating)
    elif command == 'Update':
        plant, new_rarity = input_line[1].split(' - ')
        new_rarity = float(new_rarity)
        if plant not in plants:
            print('error')
            continue
        plants[plant]['rarity'] = new_rarity
    elif command == 'Reset':
        plant = input_line[1]
        if plant not in plants:
            print('error')
            continue
        else:
            plants[plant]['rating'] = []

print(f"Plants for the exhibition:")
for plant in plants:
    if plants[plant]['rating']:
        # print(plants[plant]['rating'])
        average_rating = sum(plants[plant]['rating'])/len(plants[plant]['rating'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {int(plants[plant]['rarity'])}; Rating: {average_rating:.2f}")




