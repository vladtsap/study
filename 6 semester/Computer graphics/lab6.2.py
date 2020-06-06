show_process = False


import turtle
if not show_process:
	turtle.tracer(0)


def tree(branchLen,t):
    if branchLen >= 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-12,t)
        t.left(40)
        tree(branchLen-12,t)
        t.right(20)
        t.backward(branchLen)


t = turtle.Turtle()
t.left(90)
t.up()
t.backward(100)
t.down()
tree(100,t)


turtle.update()
turtle.exitonclick()
