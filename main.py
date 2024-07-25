import turtle
from objects import Lines, Draw
from logic import change_player


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

def on_click(x, y):
    global current_player
    change_player(x, y, current_player)
    current_player = "O" if current_player == "X" else "X"

# Game mechanism
screen.onscreenclick(on_click)

# Run the turtle screen main loop
turtle.mainloop()