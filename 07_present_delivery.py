presents = int(input())
n = int(input())
matrix = list()
santa = list()
nice_kids = list()
nice_kids_with_present = 0



for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids.append([row, col])

moves = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

while ((direction := input())  != "Christmas morning") and direction != "":
    row = santa[0] + moves[direction][0]
    col = santa[1] + moves[direction][1]

    if  row < 0 or row >= n or col < 0 or col >= n:
        continue



    # if matrix[row][col] == "X":
    #     matrix[row][col] = "-"
    #     santa = [row, col]
    #     continue
    # elif matrix[row][col] == "-"
    #     matrix[row][col] = "S"
    #     matrix[][col] = "-"
    if matrix[row][col] == "V":
        presents -= 1
        nice_kids.remove([row, col])
        nice_kids_with_present += 1
    elif matrix[row][col] == "C":
        for dir, steps in moves.items():
            r = row + steps[0]
            c = col + steps[1]
            if 0 <= r < n and 0 <= c < n:
                if matrix[r][c] in "VX" and presents > 0:
                    presents -= 1
                    nice_kids_with_present += 1
                    if matrix[r][c] == "V":
                        nice_kids.remove([r, c])
                    matrix[r][c] = "-"


    matrix[row][col] = "S"
    matrix[santa[0]][santa[1]] = "-"
    santa = [row, col]
    if not presents:
        break

if nice_kids and presents <= 0:
    print(f"Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids:
    print(f"No presents for {len(nice_kids)} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_with_present} happy nice kid/s.")




