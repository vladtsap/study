show_process = False
iterations = 50


import turtle
if not show_process:
    turtle.tracer(0)


def fern(length):
    if length <= 0.50:
        turtle.fd(length)
        turtle.bk(length)
    else:
        turtle.fd(length)          
        turtle.lt(90)
        fern(length * 0.35)

        turtle.rt(180)
        fern(length * 0.35)

        turtle.lt(90)              
        turtle.lt(3)
        fern(length * 0.87)

        turtle.rt(3)
        turtle.bk(length)

turtle.colormode(255)
turtle.color((0, 150, 0))
turtle.penup()
turtle.goto(-330, 0)
turtle.pendown()
fern(iterations)


turtle.update()
turtle.exitonclick()
