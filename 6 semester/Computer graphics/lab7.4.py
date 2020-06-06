show_process = False
iterations = 50


import turtle
if not show_process:
    turtle.tracer(0)


def draw_partial_fern(t, size, angle, c1, c2):
    t.left(angle)
    draw_fern(t, size * c1)
    t.right(angle)
    t.backward(size * c2)

def draw_fern(t, size):
    if size > 1:
        t.forward(size)
        draw_partial_fern(t, size, 5, 0.8, 0.05)
        draw_partial_fern(t, size, -40, 0.45, 0.2)
        draw_partial_fern(t, size, 35, 0.4, 0.75)

t = turtle.Turtle()
t.hideturtle()
t.left(90)
draw_fern(t, iterations)


turtle.update()
turtle.exitonclick()
