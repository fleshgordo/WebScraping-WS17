import axi
import time
from random import randint
d = axi.Device()
d.enable_motors()

turtle = axi.Turtle()

##turtle.goto(0,0)
#
#turtle.pd()
#turtle.pu()

turtle.goto(5,3)

for i in range(100):
    zustand = randint(1,3)
    distanz = 0.2
    print zustand
    if zustand == 1:
        # turtle gehe nach links
        turtle.lt(90)
        turtle.forward(distanz)
    elif zustand == 2:
        turtle.forward(distanz)
    elif zustand == 3:
        turtle.rt(90)
        turtle.forward(distanz)
    #elif zustand == 4:
    #    turtle.backward(distanz)

drawing = turtle.drawing
axi.draw(drawing)
d.disable_motors()
