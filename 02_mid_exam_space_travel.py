travel_route = input().split("||")
fuel_starting_amount = int(input())
ammunition_starting_amount = int(input())

for action in travel_route:
    action_temp = action.split(" ")
    command = action_temp[0]
    if command == "Travel":
        light_years = int(action_temp[1])
        if fuel_starting_amount >= light_years:
            fuel_starting_amount -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print(f"Mission failed.")
            exit()
    elif command == "Enemy":
        enemy_armor = int(action_temp[1])
        if ammunition_starting_amount >= enemy_armor:
            ammunition_starting_amount -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            if fuel_starting_amount >= (enemy_armor * 2):
                fuel_starting_amount -= (enemy_armor * 2)
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print(f"Mission failed.")
                exit()
    elif command == "Repair":
        fuel_added = int(action_temp[1])
        fuel_starting_amount += fuel_added
        ammunitions_added = 2 * int(action_temp[1])
        ammunition_starting_amount += ammunitions_added
        print(f"Ammunitions added: {ammunitions_added}.")
        print(f"Fuel added: {fuel_added}.")
    elif command == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        exit()
