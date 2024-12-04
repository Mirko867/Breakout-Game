from turtle import Turtle


class Ball(Turtle):

    def __init__(self, level):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 10*level

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self, level):
        self.goto(0, 0)
        self.move_speed = 10*level
        self.bounce_x()
        self.bounce_y()
