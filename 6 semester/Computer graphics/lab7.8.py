show_process = False
iterations = 11


import turtle
if not show_process:
    turtle.tracer(0)


def draw_tree(branch_length, level, width):
    branch_length *= 0.75
    new_width = width * 0.75

    turtle.width(new_width)
    turtle.left(27)
    turtle.forward(branch_length)

    if level > 0:
        draw_tree(branch_length, level - 1, new_width)

    turtle.back(branch_length)
    turtle.right(54)
    turtle.forward(branch_length)

    if level > 0:
        draw_tree(branch_length, level - 1, new_width)

    turtle.back(branch_length)
    turtle.left(27)
    turtle.width(width)

turtle.hideturtle()
turtle.left(90)
turtle.width(15)
turtle.penup()
turtle.back(180)
turtle.pendown()
turtle.forward(120)

draw_tree(120, iterations, 15)


turtle.update()
turtle.exitonclick()
