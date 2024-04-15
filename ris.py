import turtle


class Chess:

    def __init__(self):
        print('chess')
        self.t = turtle.Turtle()
        turtle.tracer(0)
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = 'black'
                else:
                    color = 'white'
                self.square(-200 + i * 50, -200 + j * 50, 50, color)

    def square(self, x, y, size, color):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.color(color)
        self.t.begin_fill()

        for i in range(4):
            self.t.forward(size)
            self.t.left(90)

        self.t.end_fill()

    def Ferz(self, x, y, color):
        t = self.t
        t.penup()
        t.goto(x + 12, y + 12)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()

        t.forward(24)
        t.left(80)
        t.forward(22)
        t.left(130)
        t.forward(10)
        t.right(70)
        t.forward(10)
        t.left(85)
        t.forward(10)
        t.right(80)
        t.forward(10)
        t.left(135)
        t.forward(22)
        t.left(80)

        t.end_fill()

    def mainloop(self):
        turtle.mainloop()


'''
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            Ferz(-200 + i * 50, -200 + j * 50, 'red')
        else:
            Ferz(-200 + i * 50, -200 + j * 50, 'blue')



turtle.mainloop()
'''
