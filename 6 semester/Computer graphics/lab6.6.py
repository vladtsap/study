show_process = False
iterations = 300


import turtle
import math
if not show_process:
	turtle.tracer(0)


turtle.lt(1.5)
for i in range(iterations):
    turtle.forward(i / math.pi)
    turtle.left(i / math.pi)
    turtle.forward(i / math.pi)
    turtle.right(i / math.pi)
    turtle.forward(i / 2)
    turtle.right(72)


turtle.update()
turtle.exitonclick()
