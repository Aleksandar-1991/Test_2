import tkinter as tk
import time

def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for row in range(rows)]

def handle_column_click(ma, labels, column_num, player, rows, cols, slots):
    pass

game_state = {
    "player_num": 1,
    "counter": 0
}

def on_click(column_number, state ):
    state["player_num"], state["counter"] = handle_column_click(matrix, labels, column_number, )

def create_ui(root, rows, cols, slots):
    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text= " ", bg = "white", relief="solid", width=4, height=2 ) for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row = r + 1, column = c)
    buttons = [tk.Button(root, text= "↓", width=4, height=2, bg="yellow", command= lambda c_idx: pass) for _ in range(cols)]
    for col, button in enumerate(buttons):
        button.grid(row = 0, column = col)

def start_game():
    root = tk.Tk()
    root.title("Connect Four")
    time.sleep(1)
    rows, cols, slots_to_win = 6, 7, 4
    create_ui(root, rows, cols, slots_to_win)
    root.mainloop()

if __name__ == "__main__":
    start_game()