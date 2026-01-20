SIZE = 5
matrix = list()
my_position = list()
targets_counter = 0
targets_down = list()

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets_counter += 1
possible_moves = {
    "left": (0 , -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for i in range(int(input())):
    user_input = input().split()
    command = user_input[0]
    direction = user_input[1]
    if command == "shoot":
        row = my_position[0] + possible_moves[direction][0]
        col = my_position[1] + possible_moves[direction][1]

        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets_counter -= 1
                targets_down.append([row, col])
                break
            row += possible_moves[direction][0]
            col += possible_moves[direction][1]

        if not targets_counter:
            print(f"Training completed! All {len(targets_down)} targets hit.")

    elif command == "move":
        steps = int(user_input[2])
        row = my_position[0] + possible_moves[direction][0] * steps
        col = my_position[1] + possible_moves[direction][1] * steps

        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == ".":
            matrix[row][col] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [row, col]

if targets_counter:
    print(f"Training not completed! {targets_counter} targets left.")
[print(row) for row in targets_down]