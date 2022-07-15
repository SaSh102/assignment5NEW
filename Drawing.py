import turtle
import time
import math

pi= math.pi
win = turtle.Screen()
win.setup(700, 700)
win.bgcolor("sky blue")

pen = turtle.Pen()
x = -10
size = 20

for i in range(1, 50):
    for j in range(i+2):
        pen.forward(size)
        pen.left(float(360/(i+2)))
        height= float(100/2*math.tan(pi/ i+2))
    pen.penup()
    pen.setpos(i, x)
    pen.goto(i+x, x)
    pen.pendown()
    x -= 10
    size += 20
win.mainloop()

time.sleep(15)