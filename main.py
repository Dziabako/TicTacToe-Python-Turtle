import turtle
from objects import Lines
from logic import change_player, check_win


# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle TicTacToe")
screen.setup(width=900, height=700)
screen.listen()

# Create vertical and horizontal lines
line = Lines()
line.draw_horizontal_line(-250, 100, 500)
line.draw_horizontal_line(-250, -100, 500)
line.draw_vertical_line(-100, -250, 500)
line.draw_vertical_line(100, -250, 500)

# Create player variable
current_player = "X"

# Initialize the board
board = [['' for _ in range(3)] for _ in range(3)]

def get_board_position(x, y):
    """Convert screen coordinates to board position."""
    row = 0 if y > 100 else 1 if y > -100 else 2
    col = 0 if x < -100 else 1 if x < 100 else 2
    return row, col

def on_click(x, y):
    global current_player
    row, col = get_board_position(x, y)
    
    # Check if the position is already occupied
    if board[row][col] == '':
        change_player(x, y, current_player)
        board[row][col] = current_player
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Position already occupied!")

# Game mechanism
screen.onscreenclick(on_click)
ongoing = True

while ongoing:
    screen.update()
    if check_win(board, current_player):
        print(f"{current_player} wins!")
        ongoing = False
    elif all(all(cell != '' for cell in row) for row in board):
        print("It's a draw!")
        ongoing = False

# Run the turtle screen main loop
turtle.mainloop()