health = 100
bitcoins = 0
rooms = input().split("|")
best_room = int()

for room in rooms:
    current_room = room.split(" ")
    action = current_room[0]
    points = int(current_room[1])
    if action == "potion":
        if (health + points) > 100:
            healed_point = 100 - health
            health = 100
            print(f"You healed for {healed_point} hp.")
            print(f"Current health: {health} hp.")
        else:
            health += points
            print(f"You healed for {points} hp.")
            print(f"Current health: {health} hp.")
        best_room += 1
    elif action == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")
        best_room += 1

    else:
        if (health - points) > 0:
            health -= points
            print(f"You slayed {action}.")
            best_room += 1
        else:
            health = 0
            best_room += 1
            print(f"You died! Killed by {action}.")
            print(f"Best room: {best_room}")
            break

if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

