from turtle import *
from colorsys import *
setposition(0, 90)
speed(0)
bgcolor('black')
pensize(2)
h = 0.7

for i in range(140):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.003
    circle(150 - i, 90)
    lt(90)
    lt(20)
    circle(150 - i, 90)
    lt(18)

hideturtle()
done()
