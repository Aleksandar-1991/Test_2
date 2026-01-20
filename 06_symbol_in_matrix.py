n = int(input())
matrix = list()
for i in range(n):
    row_data = list(input())
    matrix.append(row_data)

symbol = input()
position = None

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == symbol:
            position = (i, j)
            print(position)
            exit()

print(f"{symbol} does not occur in the matrix")