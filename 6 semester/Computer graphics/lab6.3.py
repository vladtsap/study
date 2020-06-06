show_process = False


import turtle
import random
if not show_process:
    turtle.tracer(0)


def tree(size, origsize):
    if size > 0:
        turtle.forward(size)
        r = random.randint(12, 30) if origsize < size else 24
        l = random.randint(12, 30) if origsize < size else 24
        turtle.right(r)
        tree(size - random.randint(7, 10), origsize)
        turtle.left(r + l)
        tree(size - random.randint(7, 10), origsize)
        turtle.right(l)
        turtle.backward(size)


turtle.penup()
turtle.ht()
turtle.left(90)
turtle.backward(140)
turtle.pendown()
tree(64, 64)


turtle.update()
turtle.exitonclick()