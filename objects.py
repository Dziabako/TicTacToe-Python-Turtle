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