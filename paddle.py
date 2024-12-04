from turtle import Turtle

class Paddle(Turtle):

    def __init__(self , position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.2 , stretch_len=2)
        self.penup()
        self.goto(position)

    def go_left(self):
        if self.xcor() > -220:
            new_x = self.xcor() - 20
            self.goto(new_x , self.ycor())

    def go_right(self):
        if self.xcor() < 220:
            new_x = self.xcor() + 20
            self.goto(new_x , self.ycor())
