show_process = False
iterations = 5
size = 25
R = 'R'
L = 'L'
old = R
new = old


import turtle
if not show_process:
    turtle.tracer(0)


for __ in range(iterations):
    new = (old) + (R)
    old = old[::-1]

    for char in range(0, len(old)):
        if old[char] == R:
            old = (old[:char]) + (L) + (old[char + 1:])
        elif old[char] == L:
            old = (old[:char]) + (R) + (old[char + 1:])
    new = (new) + (old)
    old = new

for move in range(0,len(new)):
    if new[move] == "L":
        turtle.left(90)
        turtle.forward(size)
    elif new[move] == "R":
        turtle.right(90)
        turtle.forward(size)


turtle.update()
turtle.exitonclick()
