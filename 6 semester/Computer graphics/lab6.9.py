show_process = False
iterations = 500


import turtle
if not show_process:
    turtle.tracer(0)


for i in range(500):
    turtle.forward(i)
    turtle.left(91)


turtle.update()
turtle.exitonclick()
