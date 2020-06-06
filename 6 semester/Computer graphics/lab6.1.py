show_process = False
koch_set = "F-F-F"
iterations = 5


import turtle
if not show_process:
	turtle.tracer(0)


for i in range(iterations):
    koch_set = koch_set.replace("F","F+F-F+F")

for move in koch_set:
    if move == "F":
        turtle.forward(100.0 / (3 ** (iterations - 1)))
    elif move == "+":
        turtle.left(60)
    elif move == "-":
        turtle.right(120)


turtle.update()
turtle.exitonclick()
