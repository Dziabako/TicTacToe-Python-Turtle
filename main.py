import turtle
from objects import Lines
from logic import on_click, get_board_position


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
ongoing = True

# Initialize the board
board = [['' for _ in range(3)] for _ in range(3)]

# Wrapper function made for handling function with multiple variables
# X and Y are taken from cursor position on click
def wrapper_on_click(x, y):
    global board, current_player, ongoing
    board, current_player, ongoing = on_click(x, y, board, current_player, ongoing)


# Game mechanism
screen.onscreenclick(wrapper_on_click)


while ongoing:
    screen.update()
    

# Run the turtle screen main loop
turtle.mainloop()