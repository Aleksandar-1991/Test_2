n = int(input())

matrix = list()
alice = list()

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            alice = [row, col]
            matrix[row][col] = "*"

collected_tea_bags = 0
possible_moves = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

while collected_tea_bags < 10:
    direction = input()
    r, c = possible_moves[direction]
    row = alice[0] + r
    col = alice[1] + c

    if row < 0 or row >= n or col < 0 or col >= n:
        break

    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    elif matrix[row][col] not in "*.":
        collected_tea_bags += int(matrix[row][col])

    matrix[row][col] = "*"
    alice = [row, col]

if collected_tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]