maze_lines = int(input())
moves = 0
white_spaces = 0
kate_visible = False
open_way = False

for line in range(maze_lines):
    row = input()
    if " " in row:
        moves += 1
    else:
        moves = 0
        kate_visible = False
    if "k" in row:
        kate_visible = True
        open_way = True
        moves += 1
    if kate_visible == True and " " not in row:
        kate_visible = False

if kate_visible and open_way:
    print(f"Kate got out in {moves+1} moves")
else:
    print("Kate cannot get out")


