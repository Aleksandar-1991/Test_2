rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for row in range(rows)]
max_sum = float('-inf')
sub_matrix = [[], [], []]




for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i+2][j + 2]
        if max_sum < current_sum:
            max_sum = current_sum
            sub_matrix[0] = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]]
            sub_matrix[1] = [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]]
            sub_matrix[2] = [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]

print(f"Sum = {max_sum}")
for i in range(3):
    print(*sub_matrix[i])

