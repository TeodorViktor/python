
import random
from turtletest import Turtle, Screen
from random import randint

t = Turtle()
t.shape("turtletest.py")
t.color("red", "green")


# side = 3
#
# i = 0
#
# while side != 0 and side < 15:
#     angle = 360 / side
#     for i in range(side):
#         t.forward(100)
#         t.right(angle)
#         i += 1
#         if side == i:
#             rand = randint(100000, 999999)
#             t.color(f"#{rand}")
#             side += 1


# def create_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         t.forward(100)
#         t.right(angle)
#
#
# for shape_sides in range(3, 11):
#     create_shape(shape_sides)
#     rand = randint(100000, 999999)
#     t.color(f"#{rand}")




for _ in range(100):
    rand = randint(100000, 999999)
    t.color(f"#{rand}")
    t.pensize(5)
    t.speed(10)
    t.forward(30)
    angle = random.choice([0, 90, 180, 270])
    t.setheading(angle)




screen = Screen()
screen.exitonclick()