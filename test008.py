import tkinter as tk
from tkinter import mainloop


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


def is_winner(mat, r, c, p_num, slots ):
    return any([
        is_vertical_win(mat, r, c, p_num, slots),
        is_horizontal_win(mat, r, c, p_num, slots),
        is_right_diagonal_win(mat, r, c, p_num, slots),
        is_left_diagonal_win(mat, r, c, p_num, slots)

    ])

def handle_column_click(mat,labels, current_c, player_num, counter, rows, cols, slots):
    pass


def create_ui(root, mat_r, mat_c, slots):
    matrix = create_matrix(mat_r, mat_r)
    labels = [[tk.Label(root, text=" ", bg= "white", relief="solid", width=4, height=2) for _ in range(mat_c)] for _ in range(mat_r)]
    for row in range(mat_r):
        for col in range(mat_c):
            labels[row][col].grid(row=row + 1, column=col)

    game_state = {"player_num": 1, "counter": 0}

    def on_click(col_num, state ):
        state["player_num"], state["counter"] = handle_column_click(
            matrix, labels, col_num, state["player_num"], state["counter"], mat_r, mat_c, slots
        )

    buttons = [tk.Button(root, text="↓", width=4, height=2, background="yellow", command= lambda c_index: pass) for _ in range(mat_c)]
    for idx, button in enumerate(buttons):
        button.grid(row=0, column= idx)




    # l = tk.Label(root, text="My label")
    # l.grid(row=0, column=0)

    # b = tk.Button(root, text="Enter")
    # b.grid(row=1, column=0)

def start_game():
    root = tk.Tk()
    root.title("Connect Four")
    root.eval('tk::PlaceWindow . center')
    SLOTS_TO_WIN = 4
    matrix_rows = 6
    matrix_cols = 7
    create_ui(root, matrix_rows, matrix_cols, SLOTS_TO_WIN)
    root.mainloop()


if __name__ == "__main__":
    start_game()

    