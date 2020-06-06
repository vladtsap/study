show_process = False
iterations = 50


import turtle
if not show_process:
    turtle.tracer(0)


for i in range(iterations):
    turtle.forward(i * 10)
    turtle.right(144)


turtle.update()
turtle.exitonclick()
