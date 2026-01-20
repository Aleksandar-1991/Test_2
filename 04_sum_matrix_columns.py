rows, cols = list(map(int, input().split(", ")))

matrix = list()
for i in range(rows):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

for i in range(cols):
    total_sum = 0
    for j in range(rows):
        total_sum += matrix[j][i]
    print(total_sum)
