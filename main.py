# Using Python Turtle, build a clone of the 80s hit game Breakout.

from turtle import Screen , Turtle , Shape , shape , register_shape
from paddle import Paddle
from ball import Ball
from bloks import Bloks
from scoreboard import Scoreboard
import time
import pygame

# # Initialize Pygame for sound effects
# pygame.init()
# bounce_sound = pygame.mixer.Sound("bounce.wav")
# block_sound = pygame.mixer.Sound("block.wav")

# def play_sound(sound):
#     sound.play()

level = 1
colors = rgb_color = [ (202 , 164 , 109) , (238 , 240 , 245) , (150 , 75 , 49) , (223 , 201 , 135) ,
                           (52 , 93 , 124) ,
                           (172 , 154 , 40) , (140 , 30 , 19) , (133 , 163 , 185) , (198 , 91 , 71) ,
                           (46 , 122 , 86) ,
                           (72 , 43 , 35) , (145 , 178 , 148) , (13 , 99 , 71) , (233 , 175 , 164) ,
                           (161 , 142 , 158) ,
                           (105 , 74 , 77) , (55 , 46 , 50) , (183 , 205 , 171) , (36 , 60 , 74) , (18 , 86 , 90) ,
                           (81 , 148 , 129) , (148 , 17 , 20) , (14 , 70 , 64) , (30 , 68 , 100) ,
                           (107 , 127 , 153) ,
                           (174 , 94 , 97) , (176 , 192 , 209) ]

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=400, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0,-250))
ball = Ball(level=level)
scoreboard = Scoreboard()

# Creating the blocks
# initial_coordinate = (-300.00 , 130.00)
bloks = Bloks(colors=colors)

screen.listen()

screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor()> 180 or ball.xcor() < -180:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 20 and ball.ycor() < -230:
        # play_sound(bounce_sound)
        ball.bounce_y()

    # # Detect collision with one block
    for block in bloks.list:
        if ball.distance(block) < 20:
            # play_sound(block_sound)
            block.goto(1000 , 1000)
            bloks.list.remove(block)
            ball.bounce_y()
            scoreboard.increase_score()

    # Check if all blocks are cleared
    if not bloks.list:
        level += 1
        scoreboard.level = level
        ball.reset_position(level=level)
        bloks = Bloks(colors=colors)
        ball.move_speed *= 0.9  # Increase ball speed for the next level

    # Detect paddle misses
    if ball.ycor() < -280:
        ball.reset_position(level=level)
        scoreboard.decrease_lives()
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_is_on = False
        # scoreboard.l_point()

screen.exitonclick()
