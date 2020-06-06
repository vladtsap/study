show_process = False


import turtle 


class SierpinskiCarpet:
    def __init__(self, baseLength=400, levels=5, bgcolor='black', pencolor='green'):
        self.baseLength = baseLength
        self.levels = levels
        self.bgcolor = bgcolor
        self.pencolor = pencolor

        self.t = turtle.Pen()
        screen = self.t.getscreen()
        screen.bgcolor(self.bgcolor)
        self.t.color(self.pencolor)
        self.resetPos((-200,200))

    def resetPos(self, coordinates):
        self.t.up()
        self.t.setpos(coordinates[0], coordinates[1])
        self.t.down()

    def endThis(self):
        turtle.done()

    def drawSquare(self, coordinates, length):
        self.resetPos(coordinates)
        self.t.heading = 0
        self.t.begin_fill()
        for i in range (0,4):
            self.t.forward(length)
            self.t.right(90)        
        self.t.end_fill()

    def iterate(self, coordinates, level):
        if level > self.levels:
            return
        innerLength = self.baseLength/(3**level)
        inner_x = coordinates[0]+innerLength
        inner_y = coordinates[1]-innerLength
        self.drawSquare((inner_x, inner_y), innerLength)

        for i in range(0,3):
            for j in range(0,3):
                if (i!=1) or (j!=1):
                    new_x = coordinates[0]+i*innerLength
                    new_y = coordinates[1]-j*innerLength
                    self.iterate((new_x, new_y), level+1)

    def display(self):
        leftCorner = (-200, 200)
        self.resetPos(leftCorner)
        self.t.color('green')
        self.t.begin_fill()
        for i in range(0, 4):
            self.t.forward(self.baseLength)
            self.t.right(90)
        self.t.end_fill()
        self.t.color(self.bgcolor)
        self.iterate(leftCorner, 1)
        self.endThis()

if __name__ == '__main__':

    if not show_process:
        turtle.tracer(0)

    s = SierpinskiCarpet()
    s.display()

    turtle.update()
    turtle.exitonclick()
