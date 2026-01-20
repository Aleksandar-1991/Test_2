rows, cols = [int(x) for x in input().split()]

matrix = list()

for i in range(rows):
    row_data = list()
    for j in range(cols):
       current_item = chr(i + 97) + chr(i + j + 97) +  chr(i + 97)
       row_data.append(current_item)
    matrix.append(row_data)


[print(*matrix[row]) for row in range(rows)]
 