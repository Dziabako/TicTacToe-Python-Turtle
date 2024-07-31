import turtle
from objects import Lines, Title, Text, Reset
from logic import on_click


# Create a turtle screen
# This way we can reset the board easier
def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Turtle TicTacToe")
    screen.setup(width=700, height=800)
    screen.listen()
    return screen

screen = setup_screen()


# Create vertical and horizontal lines
# Its a func because later is being used to reset the board
line = Lines()
def draw_board():
    line.draw_horizontal_line(-250, 100, 500)
    line.draw_horizontal_line(-250, -100, 500)
    line.draw_vertical_line(-100, -250, 500)
    line.draw_vertical_line(100, -250, 500)


# Create Title
title = Title()
text = Text()
reset = Reset()


# Define the boundaries of the board to prevent player from clicing outside the board
BOARD_MIN_X = -250
BOARD_MAX_X = 250
BOARD_MIN_Y = -250
BOARD_MAX_Y = 250


# Create player variable
current_player = "X"
ongoing = True
# This way player turn is displayed at the beggining
text.display_player_turn(current_player)


# Initialize the board
board = [['' for _ in range(3)] for _ in range(3)]


# Game mechanism
def setup_game():
    global board, current_player, ongoing, screen
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = "X"
    ongoing = True
    text.clear_text()
    text.display_player_turn(current_player)
    draw_board()
    screen.onscreenclick(wrapper_on_click)


# Reset game
# Func has to take x and y as arguments because it is called by on_click() which takes x and y as arguments
def reset_game(x=None, y=None):
    global screen
    turtle.clearscreen()
    screen = setup_screen()
    # Func draw_board() and title are called again to ensure that board and title will be displayed
    draw_board()
    title = Title()
    setup_game()


# Wrapper function made for handling function with multiple variables
# X and Y are taken from cursor position on click
def wrapper_on_click(x, y):
    global board, current_player, ongoing

    if not ongoing:
        return  # Do nothing if the game is finished
    if x < BOARD_MIN_X or x > BOARD_MAX_X or y < BOARD_MIN_Y or y > BOARD_MAX_Y:
        return  # Do nothing if the click is outside the board
    
    board, current_player, ongoing = on_click(x, y, board, current_player, ongoing)
    
    # This way the current player is displayed
    if ongoing:
        text.display_player_turn(current_player)
    else:
        text.clear_text()
        reset.show_reset_button(reset_game)

# Starting game without while function
setup_game()
    
    
# Run the turtle screen main loop
turtle.mainloop()