rows = cols = int(input())

matrix = list()
knights = list()
removed = set()
for r in range(rows):
    row_data = list(input())
    for c in range(cols):
        if row_data[c] == "K":
            knights.append((r, c))
    matrix.append(row_data)



def check_knight(mat, k_r, k_c, knights_list):
    attacked_knights = 0
    positions = [
        (-2, -1),
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, 1),
        (1, -2),
        (-1, -2)
    ]
    for (a_row, a_col) in positions:
        current_row, current_col = a_row + k_r, a_col + k_c
        if (current_row, current_col) in knights_list:
            attacked_knights += 1
    return mat, attacked_knights


while True:
    most_dangerous_knight_row = int()
    most_dangerous_knight_col = int()
    knights_under_attack = 0
    for (r, c) in knights:
        current_knight = matrix[r][c]
        matrix, attacked_fields = check_knight(matrix, r, c, knights)
        if attacked_fields > knights_under_attack:
            knights_under_attack = attacked_fields
            most_dangerous_knight_row = r
            most_dangerous_knight_col = c
    if knights_under_attack:
        matrix[most_dangerous_knight_row][most_dangerous_knight_col] = "0"
        knights.remove((most_dangerous_knight_row, most_dangerous_knight_col))
        removed.add((most_dangerous_knight_row, most_dangerous_knight_col))
    else:
        break
print(len(removed))



