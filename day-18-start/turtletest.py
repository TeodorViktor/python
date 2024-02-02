import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def cir(gap):
    for _ in range(int(360 / gap)):
        timmy.circle(100)
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + gap)



i = 0

def cir_2():
    global i

    for _ in range(70):
        timmy.circle(100)
        timmy.pencolor(random_color())
        timmy.right(i)
        i += 5
cir_2()
cir(5)
screen = Screen()
screen.exitonclick()
