SLOTS_TO_WIN = 4
matrix_rows = 6
matrix_cols = 7

class InvalidColumnError(Exception):
    pass

class InvalidValueError(Exception):
    pass

class FullColumnError(Exception):
    pass

def create_matrix(r, c):
    return [[0 for j in range(c)] for _ in range(r)]

def validate_column_choice(num, col_max_index):
    if not (0 <= num < col_max_index):
        raise InvalidColumnError

def place_player_choice(ma , c, p_num):
    for r in range(len(ma) -1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = p_num
            return r, c
    else:
        raise FullColumnError

def print_matrix(m):
    return [print(row) for row in matrix]

def is_player_num(m, r, c, p_num):
    try:
        return m[r][c] == p_num
    except IndexError:
        return False

def is_vertical_win(mat, r, c, p_num, slots):
    return all(is_player_num(mat, r + idx, c, p_num) for idx in range(slots))

def is_horizontal_win(mat, r, c, p_num, slots):
    filled_slots = 1

    for idx in range(1,slots):
        if is_player_num(mat, r, c + idx, p_num):
            filled_slots += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(mat, r, c - idx, p_num):
            filled_slots += 1
        else:
            break

    if filled_slots >= slots:
        return True
    else:
        return False
def is_right_diagonal_win(mat, r, c, p_num, slots):
    filled_slots = 1

    for idx in range(1, slots):
        if is_player_num(mat, r - idx, c + idx, p_num):
            filled_slots += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(mat, r + idx, c - idx, p_num):
            filled_slots += 1
        else:
            break

    if filled_slots >= slots:
        return True
    else:
        return False

def is_left_diagonal_win(mat, r, c, p_num, slots):
    filled_slots = 1

    for idx in range(1, slots):
        if is_player_num(mat, r + idx, c + idx, p_num):
            filled_slots += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(mat, r - idx, c - idx, p_num):
            filled_slots += 1
        else:
            break

    if filled_slots >= slots:
        return True
    else:
        return False


def is_winner(mat, r, c, p_num, slots = SLOTS_TO_WIN ):
    return any([
        is_vertical_win(mat, r, c, p_num, slots),
        is_horizontal_win(mat, r, c, p_num, slots),
        is_right_diagonal_win(mat, r, c, p_num, slots),
        is_left_diagonal_win(mat, r, c, p_num, slots)

    ])



matrix = create_matrix(matrix_rows, matrix_cols)

current_player = 1
counter = 0

while True:
    current_player = 2 if current_player % 2 == 0 else 1
    try:
        chosen_column = int(input(f"Player {current_player}, please choose a column:")) - 1
        validate_column_choice(chosen_column, matrix_cols)
        current_row, current_col = place_player_choice(matrix, chosen_column, current_player)
        print_matrix(matrix)
        if is_winner(matrix, current_row, current_col, current_player):
            print(f"The winner is Player {current_player}")
            break

    except InvalidColumnError:
        print(f"Invalid column! Please choose a number between 1 and {matrix_cols}")
        continue
    except ValueError:
        print(f"Please enter a digit!")
        continue
    except FullColumnError:
        print(f"The selected column is full! Please select a different column.")
        continue


    counter += 1
    if counter == matrix_rows * matrix_cols:
        print(f"The game is draw!")
        break
    current_player += 1
# [[print(_)] for _ in matrix]





