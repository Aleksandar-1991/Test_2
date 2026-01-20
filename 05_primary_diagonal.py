n = int(input())

matrix = []

for i in range(n):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

total_sum = 0

for i in range(len(matrix)):
    total_sum += matrix[i][-(i+1)]

print(total_sum)