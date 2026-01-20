n = int(input())

matrix = list()
bunny = tuple()

for row in range(n):
    row_data = input().split()
    for col in range(n):
        if row_data[col] == "B":
            bunny = (row, col)
    matrix.append(row_data)

def check_sum_right(mat, b_r, b_c):
    right_sum = 0
    right_steps = list()
    for i in range(b_c + 1, len(mat)):
        if mat[b_r][i].isdigit():
            right_sum += int(mat[b_r][i])
            right_steps.append([b_r, i])
        elif mat[b_r][i] == "X":
            break
    return right_sum, right_steps

def check_sum_left(mat, b_r, b_c):
    left_sum = 0
    left_steps = list()
    for i in range(b_c - 1, -1, -1):
        if mat[b_r][i].isdigit():
            left_sum += int(mat[b_r][i])
            left_steps.append([b_r, i])
        elif mat[b_r][i] == "X":
            break
    return left_sum, left_steps

def check_sum_up(mat, b_r, b_c):
    up_sum = 0
    up_steps = list()
    for i in range(b_r - 1, -1, -1):
        if mat[i][b_c].isdigit():
            up_sum += int(mat[i][b_c])
            up_steps.append([i, b_c])
        elif mat[i][b_c] == "X":
            break
    return up_sum, up_steps

def check_sum_down(mat, b_r, b_c):
    down_sum = 0
    down_steps = list()
    for i in range(b_r + 1, len(mat)):
        if mat[i][b_c].isdigit():
            down_sum += int(mat[i][b_c])
            down_steps.append([i, b_c])
        elif mat[i][b_c] == "X":
            break
    return down_sum, down_steps

# max_sum = 0
# final_steps = list()

sum_left, steps_left = check_sum_left(matrix, bunny[0], bunny[1])
sum_right, steps_right = check_sum_right(matrix, bunny[0], bunny[1])
sum_up, steps_up = check_sum_up(matrix, bunny[0], bunny[1])
sum_down, steps_down = check_sum_down(matrix, bunny[0], bunny[1])

results = {
    sum_left: [steps_left, 'left'],
    sum_right: [steps_right, 'right'],
    sum_up: [steps_up, 'up'],
    sum_down: [steps_down, 'down']

}
max_sum = max(sum_down, sum_up, sum_left, sum_right)
final_steps = results[max_sum][0]
direction = results[max_sum][1]
print(direction)
for step in final_steps:
    print(step)
print(max_sum)


