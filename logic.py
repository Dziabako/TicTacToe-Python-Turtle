from objects import Draw
from objects import Text

drawer = Draw()
text = Text()


def change_player(x, y, current_player):

    # Determine the cell based on click position
    if -250 < x < -100:
        col = -175
    elif -100 < x < 100:
        col = 0
    elif 100 < x < 250:
        col = 175
    else:
        return

    if -250 < y < -100:
        row = -175
    elif -100 < y < 100:
        row = 0
    elif 100 < y < 250:
        row = 175
    else:
        return

    if current_player == "X":
        drawer.draw_x(col, row)
        current_player = "O"
    else:
        drawer.draw_o(col, row)
        current_player = "X"


def check_win(board, current_player):
    winner = ""
    if board[0][0] == board[0][1] == board[0][2] != '':
        winner = current_player
    elif board[1][0] == board[1][1] == board[1][2] != '':
        winner = current_player
    elif board[2][0] == board[2][1] == board[2][2] != '':
        winner = current_player
    elif board[0][0] == board[1][0] == board[2][0] != '':
        winner = current_player
    elif board[0][1] == board[1][1] == board[2][1] != '':
        winner = current_player
    elif board[0][2] == board[1][2] == board[2][2] != '':
        winner = current_player
    elif board[0][0] == board[1][1] == board[2][2] != '':
        winner = current_player
    elif board[0][2] == board[1][1] == board[2][0] != '':
        winner = current_player
    return winner


def get_board_position(x, y):
    """Convert screen coordinates to board position."""
    row = 0 if y > 100 else 1 if y > -100 else 2
    col = 0 if x < -100 else 1 if x < 100 else 2
    return row, col

def on_click(x, y, board, current_player, ongoing):
    row, col = get_board_position(x, y)
    
    # Check if the position is already occupied
    if board[row][col] == '':
        change_player(x, y, current_player)
        board[row][col] = current_player

        text.display_player_turn(current_player)

        if check_win(board, current_player):
            print(f"{current_player} wins!")
            text.display_winner(winner=current_player)
            ongoing = False
            print(board)
        elif all(all(cell != '' for cell in row) for row in board):
            print("It's a draw!")
            text.display_draw()
            ongoing = False
        else:
            if current_player == "O":
                current_player = "X"
                text.display_player_turn(current_player)
            else:
                current_player = "O"
                text.display_player_turn(current_player)
        return board, current_player, ongoing
    else:
        print("Position already occupied!")
