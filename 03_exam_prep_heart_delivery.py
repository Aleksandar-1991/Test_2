
neighbourhood = list(map(int, input().split("@")))

user_input = input()
current_index = int()

while user_input != "Love!":
    command = user_input.split()
    action = command[0]
    jump_length = int(command[1])
    if current_index + jump_length < len(neighbourhood):
        current_index += jump_length
    else:
        current_index = 0

    if neighbourhood[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    elif neighbourhood[current_index] - 2 == 0:
        neighbourhood[current_index] -= 2
        print(f"Place {current_index} has Valentine's day.")
    else:
        neighbourhood[current_index] -= 2
    user_input = input()

print(f"Cupid's last position was {current_index}.")
if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    failed_places = 0
    for house in range(len(neighbourhood)):
        if neighbourhood[house] > 0:
            failed_places += 1
    print(f"Cupid has failed {failed_places} places.")
