rows = cols = int(input())

matrix = list()
alive_cells = set()
alive_cells_sum = 0

for row in range(rows):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

bombs_strings = input().split()
bombs = list()
for bomb_data in bombs_strings:
    b_row, b_col = [int(x) for x in bomb_data.split(",")]
    bombs.append((b_row, b_col))


for i in range(rows):
    for j in range(cols):
        if (i, j) not in bombs:
            alive_cells.add((i, j))

def detonate(mat, b_row, b_col, bombs_list):
    power = mat[b_row][b_col]
    for r in range(b_row - 1, b_row + 2):
        if 0 <= r < rows:
            for c in range(b_col - 1, b_col + 2):
                if 0 <= c < cols:
                    if r == b_row and c == b_col:
                        mat[r][c] = 0
                    elif (r, c) in bombs_list:
                        if mat[r][c] - power < 0:
                            mat[r][c] = 0
                        else:
                            mat[r][c] -= power
                    else:
                        if mat[r][c] > 0:
                            mat[r][c] -= power
                        if mat[r][c] <= 0 and (r, c) in alive_cells:
                            alive_cells.remove((r, c))
    return mat


for (bomb_row, bomb_col) in bombs:
    matrix = detonate(matrix, bomb_row, bomb_col, bombs)
    # print("Temp mat:")
    # [print(" ".join(str(x) for x in row)) for row in matrix]


print(f"Alive cells: {len(alive_cells)}")
for (a_row, a_col) in alive_cells:
    alive_cells_sum += matrix[a_row][a_col]
print(f"Sum: {alive_cells_sum}")
[print(" ".join(str(x) for x in row)) for row in matrix]




