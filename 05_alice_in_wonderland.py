n = int(input())

matrix = list()
alice = list()

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            alice = [row, col]

tea_sum = 0
alice_made_it = False

possible_moves = {
    "left": (0, -1),
    "right": (0 , 1),
    "up": (-1, 0),
    "down": (1, 0)
}

while (command := input()) != "":
    r, l = possible_moves[command]
    matrix[alice[0]][alice[1]] = "*"
    row = alice[0] + r
    col = alice[1] + l

    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    elif matrix[row][col] == ".":
        alice = [row, col]
        matrix[row][col] = "*"
        continue
    elif matrix[row][col] == "*":
        alice = [row, col]
        continue
    elif matrix[row][col].isdigit():
        tea_sum += int(matrix[row][col])
        alice = [row, col]
        matrix[row][col] = "*"

    if tea_sum >= 10:
        alice_made_it = True
        break

if alice_made_it:
    print("She did it! She went to the party.")
else:
    print("She did it! She went to the party.")
[print(" ".join(row)) for row in matrix]


