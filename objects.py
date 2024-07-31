from turtle import Turtle


class Lines(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("white")
    
    def draw_horizontal_line(self, x, y, length):
        self.goto(x, y)
        self.pendown()
        self.setheading(0)
        self.pensize(7)  # Increase the pen size to make the line thicker
        self.forward(length)
        self.penup()

    def draw_vertical_line(self, x, y, length):
        self.goto(x, y)
        self.pendown()
        self.setheading(90)
        self.pensize(7)  # Increase the pen size to make the line thicker
        self.forward(length)
        self.penup()


class Draw:
    def __init__(self):
        self.drawer = Turtle()
        self.drawer.hideturtle()
        self.drawer.speed(0)

    def draw_x(self, x, y):
        self.drawer.color("red")
        self.drawer.pensize(5)
        self.drawer.penup()
        self.drawer.goto(x - 50, y - 50)
        self.drawer.pendown()
        self.drawer.goto(x + 50, y + 50)
        self.drawer.penup()
        self.drawer.goto(x - 50, y + 50)
        self.drawer.pendown()
        self.drawer.goto(x + 50, y - 50)

    def draw_o(self, x, y):
        self.drawer.color("blue")
        self.drawer.pensize(5)
        self.drawer.penup()
        self.drawer.goto(x, y - 50)
        self.drawer.setheading(0)
        self.drawer.pendown()
        self.drawer.circle(50)
        self.drawer.penup()


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 300)  # Adjust the x-coordinate to center the text
        self.color("white")

    def display_player_turn(self, current_player):
        self.clear()
        self.write(f"Player {current_player}'s turn", align="center", font=("Arial", 24, "normal"))  # Add align="center" to center the text

    def display_winner(self, winner):
        self.clear()
        self.write(f"Player {winner} wins!", align="center", font=("Arial", 24, "normal"))  # Add align="center" to center the text

    def display_draw(self):
        self.clear()
        self.write("It's a draw!", align="center", font=("Arial", 24, "normal"))  # Add align="center" to center the text

    def clear_text(self):
        self.clear()


class Title(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-150, 350)
        self.color("white")
        self.write("Turtle TicTacToe", font=("Arial", 24, "normal"))


class Reset():
    def show_reset_button(self, reset_game):
        reset_button = Turtle()
        reset_button.penup()
        reset_button.color("white")
        reset_button.goto(0, -300)
        reset_button.write("Reset Game", align="center", font=("Arial", 16, "normal"))
        reset_button.goto(0, -320)
        reset_button.shape("square")
        reset_button.shapesize(stretch_wid=1, stretch_len=5)
        reset_button.fillcolor("lightgray")
        reset_button.onclick(reset_game)
