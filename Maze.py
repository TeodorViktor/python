def TurnRight():
    turn_left()
    turn_left()
    turn_left()
def goUp():
    turn_left()
    while wall_on_right():
        move()
    TurnRight()
    move()
    TurnRight()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        goUp()
    else:
        move()




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
