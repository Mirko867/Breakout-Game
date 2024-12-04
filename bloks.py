import random
import turtle
from turtle import Turtle

turtle.colormode(255)


class Bloks(Turtle):

    def __init__(self, colors, t=100):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(-160, 100)
        list = []
        for x in range(1,7):
            for i in range(1 , 9):
                clone = self.clone()
                clone.color(random.choice(colors))
                list.append(clone)
                self.forward(25)
                self.forward(20)
            t = t + 30
            self.goto(-160.00 , t)
            self.penup()
        self.list = list