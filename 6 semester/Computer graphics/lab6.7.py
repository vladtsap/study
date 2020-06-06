show_process = False
iterations = 6
step = 5
angle = 90

import turtle
if not show_process:
    turtle.tracer(0)


def hilbert(rule, depth, t):
    if depth > 0:
        a = lambda: hilbert("a", depth - 1, t)
        b = lambda: hilbert("b", depth - 1, t)
        left = lambda: t.left(angle)
        right = lambda: t.right(angle)
        forward = lambda: t.forward(step)
        if rule == "a":
            left();
            b();
            forward();
            right();
            a();
            forward();
            a();
            right();
            forward();
            b();
            left();
        if rule == "b":
            right();
            a();
            forward();
            left();
            b();
            forward();
            b();
            left();
            forward();
            a();
            right();

t = turtle.Turtle()
hilbert("a", iterations, t)

turtle.update()
turtle.exitonclick()
