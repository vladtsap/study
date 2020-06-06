show_process = False
iterations = 8


import turtle
if not show_process:
    turtle.tracer(0)


def triangle(t, depth, maxdepth):
    if depth > maxdepth:
        return
    else:
        for i in range(3):
            t.forward(256/2**depth)
            triangle(t, depth+1, maxdepth)
            t.forward(256/(2**depth))
            t.left(120)
        return

t = turtle.Turtle()
t.penup()
t.goto(-50, -200)
t.pendown()
t.hideturtle()
t.right(180)
t.forward(256)
t.right(180)
triangle(t, 0, iterations)


turtle.update()
turtle.exitonclick()
