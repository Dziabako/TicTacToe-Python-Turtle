import turtle
from objects import Draw, Text

drawer = Draw()
text = Text()


def change_player(x, y, current_player):
    """Change the player after each turn"""

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
    
    return current_player


def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(len(board)):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][len(board) - 1 - i] == player for i in range(len(board))):
        return True
    return False


def get_board_position(x, y):
    """Convert screen coordinates to board position."""
    row = 0 if y > 100 else 1 if y > -100 else 2
    col = 0 if x < -100 else 1 if x < 100 else 2
    return row, col

def on_click(x, y, board, current_player, ongoing):
    """Base game machanics and handle clicks on screen"""
    row, col = get_board_position(x, y)
    
    # Check if the position is already occupied
    if board[row][col] == '':
        change_player(x, y, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            ongoing = False
            print(f"{current_player} wins!")
            text.display_winner(winner=current_player)
        elif all(all(cell != '' for cell in row) for row in board):
            ongoing = False
            print("It's a draw!")
            text.display_draw()
        else:
            if current_player == "O":
                current_player = "X"
            else:
                current_player = "O"
        return board, current_player, ongoing
    else:
        print("Position already occupied!")
