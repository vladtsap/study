show_process = False


import turtle
if not show_process:
	turtle.tracer(0)


def draw(x,y,n):
    n1 = n * 2/3
    if(n >= 1):
        turtle.setpos(x,y)
        turtle.pendown()
        turtle.forward(n)
        turtle.penup()
        y -= 5;
        draw(x,y,n/3)
        draw(x+n1,y,n/3)

draw(0,0,200)


turtle.update()
turtle.exitonclick()
