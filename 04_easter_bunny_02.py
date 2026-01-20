n = int(input())

matrix = list()
bunny = list()

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

max_sum_eggs = float("-inf")
final_steps = list()
final_direction = str()

possible_moves = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for direction, move in possible_moves.items():
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]
    current_sum = 0
    current_moves = list()

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break
        current_sum += int(matrix[row][col])
        current_moves.append([row, col])

        row += move[0]
        col += move[1]

    if current_sum > max_sum_eggs and current_moves:
        max_sum_eggs = current_sum
        final_steps = current_moves
        final_direction = direction

print(final_direction)
[print(row) for row in final_steps]
print(max_sum_eggs)
