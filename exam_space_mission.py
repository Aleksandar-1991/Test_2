from collections import deque


N = int(input())
matrix = list()
spaceship = list()
destination = list()
resources = 100
destination_reached = False
lost_in_space = False

for i in range(N):
    row_data = input().split()
    matrix.append(row_data)
    for j in range(N):
        if row_data[j] == "S":
            spaceship = [i, j]
        elif row_data[j] == "P":
            destination = [i, j]


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while resources:
    command = input()
    # if not command:
    #     break
    resources -= 5
    new_row = spaceship[0] + moves[command][0]
    new_col = spaceship[1] + moves[command][1]

    # print(new_row, new_col)
    # spaceship = [new_row, new_col]
    if new_row < 0 or new_row >= N  or new_col < 0 or new_col >= N:
        print("Mission failed! The spaceship was lost in space.")
        lost_in_space = True
        break
    if matrix[new_row][new_col] == "R":
        resources += 10
        if resources > 100:
            resources = 100

    elif matrix[new_row][new_col] == "M":
        resources -= 5
    elif matrix[new_row][new_col] == "P":
        destination_reached = True
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
    elif matrix[new_row][new_col] == ".":
        pass

    if matrix[spaceship[0]][spaceship[1]] not in "RP":
        matrix[spaceship[0]][spaceship[1]] = "."
    if matrix[new_row][new_col] not in "RP":
        matrix[new_row][new_col] = "S"
    spaceship = [new_row, new_col]
    if destination_reached:
        break


if resources <= 0 and not destination_reached and not lost_in_space:
    print("Mission failed! The spaceship was stranded in space.")
[print(" ".join([str(x) for x in row])) for row in matrix]



