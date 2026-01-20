from collections import deque

rows, cols = [int(x) for x in input().split()]
matrix = list()

has_won = False
has_died = False
player_row = 0
player_col = 0
bunnies = set()

directions = {
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1),
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c)
}

def bunnies_growth(mat, bunnies_set):
    new_bunnies = set()
    bunnies_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for b_row, b_col in bunnies_set:
        for d_row, d_col in bunnies_directions:
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < rows and 0 <= new_col < cols:
                mat[new_row][new_col] = "B"
                new_bunnies.add((new_row, new_col))
    return mat, bunnies_set.union(new_bunnies)

for row in range(rows):
    row_data = list(input())
    for col in range(cols):
        if row_data[col] == "P":
            player_row = row
            player_col = col
        elif row_data[col] == 'B':
            bunnies.add((row, col))
    matrix.append(row_data)

moves = list(input())
for move in moves:
    new_player_row, new_player_col = directions[move](player_row, player_col)
    matrix[player_row][player_col] = "."
    matrix, bunnies = bunnies_growth(matrix, bunnies)

    if (player_row, player_col) not in bunnies:
        matrix[player_row][player_col] = "."
    if new_player_row < 0 or new_player_row >= rows or new_player_col < 0 or new_player_col >= cols:
        has_won = True
        break

    player_row, player_col = new_player_row, new_player_col
    if matrix[player_row][player_col] == "B":
        has_died = True
        break


[print("".join(row)) for row in matrix]
if has_won:
    print(f"won: {player_row} {player_col}")
elif has_died:
    print(f"dead: {player_row} {player_col}")




