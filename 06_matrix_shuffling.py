rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for i in range(rows)]

def is_valid_index(r1, c1, r2, c2, r, c):
    return 0 <= r1 < r and 0 <= c1 < c and 0 <= r2 < r and 0 <= c2 < c

while (input_data := input()) != 'END':
    data = input_data.split()
    if data[0] != 'swap' and len(data) != 5:
        print("Invalid input!")
        continue

    indices = [i for i in data[1:]]
    invalid_index = False
    for i in indices:
        if not i.isdigit():
            invalid_index = True
            break
    if invalid_index:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in indices]
    if is_valid_index(row1, col1, row2, col2, rows, cols):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")

