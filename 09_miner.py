rows = cols = int(input())
commands = input().split()
matrix = list()

win = False
lose = False

route_end = set()
coal = set()
route_start = set()

for row in range(rows):
    row_data = input().split()
    matrix.append(row_data)
    for col in range(cols):
        char = matrix[row][col]
        if char == "e":
            route_end.add((row, col))
        elif char == "c":
            coal.add((row, col))
        elif char == "s":
            route_start = (row, col)

miner_row = route_start[0]
miner_col = route_start[1]

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}

for command in commands:
   new_miner_row, new_miner_col = directions[command](miner_row, miner_col)
   if new_miner_row < 0 or new_miner_row >= rows or new_miner_col < 0 or new_miner_col >= cols:
       continue

   miner_row, miner_col = new_miner_row, new_miner_col
   if (miner_row, miner_col) in coal:
       coal.remove((new_miner_row, new_miner_col))
       if not coal:
           print(f"You collected all coal! ({new_miner_row}, {miner_col})")
           exit()
   elif (miner_row, miner_col) in route_end:
       print(f"Game over! ({new_miner_row}, {new_miner_col})")
       exit()
   elif matrix[miner_row][miner_col] == "*":
       continue

print(f"{len(coal)} pieces of coal left. ({miner_row}, {miner_col})")





