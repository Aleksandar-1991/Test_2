rows, cols = [int(x) for x in input().split(", ")]

matrix = list()
for i in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

max_sum = float('-inf')
submatrix = list()

for i in range(rows -1 ):
    for j in range(cols -1 ):
        current_number = matrix[i][j]
        next_numer = matrix[i][j + 1]
        below_number = matrix[i + 1][j]
        diagonal_number = matrix[i + 1][j + 1]

        current_sum = current_number + next_numer + below_number + diagonal_number
        if max_sum < current_sum:
            max_sum = current_sum
            submatrix = [[current_number, next_numer], [below_number, diagonal_number]]

print(*submatrix[0])
print(*submatrix[1])
print(max_sum)



