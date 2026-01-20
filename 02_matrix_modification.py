rows = cols = int(input())
matrix = list()

for i in range(rows):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

while ( input_data := input()) != "END":
    data = input_data.split()
    command, r, c, value = data[0], int(data[1]), int(data[2]), int(data[3])
    if r < 0 or r >= rows or c < 0 or c >= rows:
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[r][c] += value
    elif command == "Subtract":
        matrix[r][c] -= value

[print(*row) for row in matrix]