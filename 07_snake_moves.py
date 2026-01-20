from collections import deque
rows, cols = [int(x) for x in input().split()]
word = deque(input())
matrix = list()

for row in range(rows):
    matrix.append([""] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = word[0]
        else:
            matrix[row][-1 -col] = word[0]
        word.rotate(-1)

[print(*row, sep="") for row in matrix]
