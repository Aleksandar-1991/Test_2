n = int(input())
free_chairs=0
game_on=True

for room in range(1, n+1):
    conf_room = input().split()
    available_chairs = len(conf_room[0])
    needed_chairs = int(conf_room[1])

    if available_chairs>needed_chairs:
        free_chairs += available_chairs - needed_chairs
    elif available_chairs<needed_chairs:
        print(f"{needed_chairs-available_chairs} more chairs needed in room {room}")
        game_on=False

if game_on==True:
    print(f"Game On, {free_chairs} free chairs left")




