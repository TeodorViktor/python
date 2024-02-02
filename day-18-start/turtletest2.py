from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=500)
height = -100
t = []
turtle_color = ["red", "yellow", "purple", "blue", "green", "orange"]
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color...")
for _ in range(6):
    timmy = Turtle(shape="turtle")
    timmy.color(turtle_color[_])
    t.append(timmy)
    timmy.penup()
    t[_].goto(x=-230, y=height)
    height += 50

is_race_on = False

if bet:
    is_race_on = True

while is_race_on:

    for i in t:
        random_distance = random.randint(0, 10)
        i.forward(random_distance)
        if i.xcor() > 200:
            is_race_on = False
            if bet != i.pencolor():
                print(f"{i.color()} You win!")
            else:
                print(f"{i.color()} You Lost")



screen.listen()
# screen.onkey(key="space", fun=move_forward)
# screen.onkey(key="Up", fun=turn_left)
# screen.onkey(key="Down", fun=turn_right)

screen.exitonclick()

