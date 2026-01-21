first_player = input("Player one name:")
second_player = input("Player two name:")

mapper = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2)
}

board =           [[" ", " ", " ", ],
                   [" ", " ", " ", ],
                   [" ", " ", " ", ]]
numerated_board = [["|", "1", "|", "2", "|", "3", "|"],
                  ["|", "4", "|", "5", "|", "6", "|"],
                  ["|", "7", "|", "8", "|", "9", "|"]]

free_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


players = {
    first_player: "",
    second_player: ""
}

def print_board(mat):
    for row in mat:
        print(" ".join(f"|{"|".join(row)}|"))

def play_option_verification(user_input):
    if user_input not in "123456789":
        return False

def check_for_winners(matrix, char, r, c):
    first_diag = [(0, 0),(1, 1), (2, 2)]
    second_diag = [(0, 2),(1, 1), (2, 0)]
    win_condition = char * len(matrix)
    temp_match = ""

    for j in range(len(matrix[r])):
        if matrix[r][j] == char:
            temp_match += char
    if temp_match == win_condition:
            return True

    temp_match = ""
    for i in range(len(matrix)):
        if matrix[i][c] == char:
            temp_match += char
    if temp_match == win_condition:
            return True

    temp_match = ""
    if (r, c) in first_diag:
        for i in range(len(matrix)):
            if matrix[i][i] == char:
                temp_match += char
        if temp_match == win_condition:
            return True

    temp_match = ""
    if (r, c) in second_diag:
        for i in range(len(matrix)):
            if matrix[i][len(matrix) - i -1] == char:
                temp_match += char
        if temp_match == win_condition:
            return True
    # print("check completed")
    return False


# winner = ""
play_options = ["O", "X"]
while not players[first_player]:
     player_one_choice = input(f"{first_player} would like to play with 'X' or 'O'?").upper()
     if player_one_choice not in play_options:
        print("Wrong option! Please choose between 'X' or 'O'.")
     else:
         players[first_player] = player_one_choice
         play_options.remove(player_one_choice)
players[second_player] = play_options[0]
play_options = ""

print("This is the numeration of the board:")
[print(" ".join(row)) for row in numerated_board]
print(f"{first_player} starts first!")

last_turn = second_player

while free_positions:
    current_player = ""
    if last_turn == second_player:
        current_player = first_player
        last_turn = first_player
    else:
        current_player = second_player
        last_turn = second_player

    while True:
        chosen_position = input(f"{current_player} choose a free position [1-9]:")
        current_symbol = players[current_player]
        if chosen_position not in free_positions:
            print("Invalid position. Please try again.")
            continue
        else:
            # mapper[chosen_position] = players[current_player]
            current_row, current_col = mapper[chosen_position]
            board[current_row][current_col] = current_symbol
            free_positions.remove(chosen_position)
            print_board(board)

            if check_for_winners(board, current_symbol, current_row , current_col):
                print(f"{current_player} is the winner!")
                exit()
            else:
                break

print("It's a draw....")















