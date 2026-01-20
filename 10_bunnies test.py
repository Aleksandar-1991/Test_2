from collections import deque
rows, cols = [int(x) for x in input().split()]
matrix = list()
player_location = []
current_bunnies = list()
for row in range(rows):
    row_data = list(input())
    for col in range(cols):
        if row_data[col] == 'P':
            player_location = [row, col]
        elif row_data[col] == 'B':
            current_bunnies.append([row, col])
    matrix.append(row_data)

moves = deque(input())

def player_move(pos: list, matr: list, mov: str):
    r = pos[0]
    c = pos[1]
    position = list()
    action = str()
    if mov == 'L':
        if c == 0:
            position = [r, c]
            action = 'escaped'
        elif 0 < c:
            if matr[r][c - 1] == "B":
                position = [r, c - 1]
                action = 'dead'
            elif matr[r][c - 1] == ".":
                matr[r][c] = "."
                matr[r][c - 1] = "P"
                position = [r, c -1]
                action = 'moved'
    elif mov == 'R':
        if c == cols - 1:
            position = [r, c]
            action = 'escaped'
        elif c < cols - 1:
            if matr[r][c + 1] == "B":
                position = [r, c + 1]
                action = 'dead'
            elif matr[r][c + 1] == ".":
                matr[r][c] = "."
                matr[r][c + 1] = "P"
                position = [r, c + 1]
                action = 'moved'
    elif mov == 'U':
        if r == 0:
            position = [r, c]
            action = 'escaped'
        elif 0 < r:
            if matr[r - 1][c] == "B":
                position = [r - 1, c]
                action = 'dead'
            elif matr[r - 1][c] == ".":
                matr[r][c] = "."
                matr[r - 1][c] = "P"
                position = [r - 1, c]
                action = 'moved'
    elif mov == 'D':
        if r == rows:
            position = [r, c]
            action = 'escaped'
        elif r < rows - 1:
            if matr[r + 1][c] == "B":
                position = [r + 1, c]
                action = 'dead'
            elif matr[r + 1][c] == ".":
                matr[r][c] = "."
                matr[r + 1][c] = "P"
                position = [r + 1, c ]
                action = 'moved'

    return [action, position]


def bunnies_grow(bunnies: list, matr: list):
    new_bunnies = list()
    player_dead = False
    for b in bunnies:
        bunny_row = b[0]
        bunny_col = b[1]
        temp_bunnies = list()
        if bunny_col > 0:
            if matr[bunny_row][bunny_col - 1] == "P":
                player_dead = True
            matr[bunny_row][bunny_col - 1] = 'B'
            temp_bunnies.append([bunny_row, bunny_col -1])
        if bunny_col < len(matr[0]) - 1:
            if matr[bunny_row][bunny_col + 1] == "P":
                player_dead = True
            matr[bunny_row][bunny_col + 1] = 'B'
            temp_bunnies.append([bunny_row, bunny_col + 1])
        if bunny_row > 0:
            if matr[bunny_row - 1][bunny_col] == 'P':
                player_dead = True
            matr[bunny_row - 1][bunny_col] = 'B'
            temp_bunnies.append([bunny_row - 1, bunny_col])
        if bunny_row < len(matr) - 1:
            if matr[bunny_row + 1][bunny_col] == 'P':
                player_dead = True
            matr[bunny_row + 1][bunny_col] = 'B'
            temp_bunnies.append([bunny_row + 1, bunny_col])
            new_bunnies.extend(temp_bunnies)
    bunnies.extend(new_bunnies)
    return [matr, bunnies, player_dead]


for move in range(len(moves)):
    # last_position = list()
    # escaped = None
    # escaped, last_position = is_escaped(player_location, matrix, moves[0])
    # dead, coord = is_dead(player_location, matrix, moves[0])
    # if escaped:
    #     temp_r, temp_c = player_location
    #     print(f"Log: last position {temp_r}{temp_c}")
    #     matrix[temp_r][temp_c] = "."
    #     matrix, current_bunnies, player_killed = bunnies_grow(current_bunnies, matrix)
    #     [print(*row, sep="") for row in matrix]
    #     print(f"won: {temp_r} {temp_c}")
    #     exit()
    # elif dead:
    #     matrix, current_bunnies, player_killed = bunnies_grow(current_bunnies, matrix)
    #     [print(*row, sep="") for row in matrix]
    #     print(f"dead: {coord[0]} {coord[1]}")
    #     exit()
    # else:
    #     temp_r, temp_c = player_location
    #     player_location = player_move(player_location, matrix, moves[0])
    #     matrix[temp_r][temp_c] = "."
    actioned, pos  = player_move(player_location, matrix, moves[0])
    if actioned == "escaped":
        matrix, current_bunnies, player_killed = bunnies_grow(current_bunnies, matrix)
        [print(*row, sep="") for row in matrix]
        print(f"won: {pos[0]} {pos[1]}")
        exit()
    elif actioned == 'dead':
        matrix, current_bunnies, player_killed = bunnies_grow(current_bunnies, matrix)
        [print(*row, sep="") for row in matrix]
        print(f"dead: {pos[0]} {pos[1]}")
        exit()
    elif actioned == 'moved':
        player_location = [pos[0], pos[1]]



    matrix,current_bunnies, player_killed = bunnies_grow(current_bunnies, matrix)
    if player_killed:
        [print(*row, sep="") for row in matrix]
        print(player_location)
        exit()
    else:
        moves.popleft()

[print(*row, sep="") for row in matrix]



