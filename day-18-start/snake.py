from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)
# t = Turtle(shape="square")
# t.color("#fff")
# d = Turtle(shape="square")
# d.color("#fff")
# d.goto(x=-20, y=0)
# f = Turtle(shape="square")
# f.color("#fff")
# f.goto(x=-40, y=0)
squares = []
x = 0
for _ in range(3):
    t = Turtle(shape="square")
    t.color("#fff")
    t.goto(x=x, y=0)
    x -= 20
    squares.append(t)
screen.update()






screen.exitonclick()