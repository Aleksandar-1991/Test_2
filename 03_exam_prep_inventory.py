pirate_ship_sections = list(map(int, input().split(">")))
warship_sections = [int(section) for section in input().split(">")]
max_health_of_a_section = int(input())
command = input().split()
stalemate = True


while command[0] != "Retire":
    action = command[0]
    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(warship_sections)):
            if (warship_sections[index] - damage) <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
            else:
                warship_sections[index] -= damage

    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if (start_index in range(len(pirate_ship_sections)) and (end_index in range(len(pirate_ship_sections))
        and (start_index<=end_index))):
            for attacked_section in range(start_index, end_index +1):
                if pirate_ship_sections[attacked_section] - damage > 0:
                    pirate_ship_sections[attacked_section] -= damage
                elif pirate_ship_sections[attacked_section] - damage<= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    exit()


    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index in range(len(pirate_ship_sections)):
            if pirate_ship_sections[index] + health > max_health_of_a_section:
                pirate_ship_sections[index] = max_health_of_a_section
            else:
                pirate_ship_sections[index] += health

    elif action == "Status":
        damaged_sections = 0
        for section_index in range(len(pirate_ship_sections)):
            if pirate_ship_sections[section_index] < max_health_of_a_section/5:
                damaged_sections += 1
        print(f"{damaged_sections} sections need repair.")
    command = input().split()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship_sections)}")
    print(f"Warship status: {sum(warship_sections)}")


