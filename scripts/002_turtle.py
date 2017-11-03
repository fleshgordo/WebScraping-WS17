import axi
import time

d = axi.Device()
d.enable_motors()

turtle = axi.Turtle()

##turtle.goto(0,0)
#
#turtle.pd()
#turtle.pu()

turtle.goto(5,1)

for i in range(360):
    print "move forward by 1"
    #turtle.pd() # pen down
    turtle.forward(0.01) # gehe 0.5inch nach vorwaerts
    turtle.rt(1) # drehe dich um 60grad
    #turtle.pu() # pen up

drawing = turtle.drawing
axi.draw(drawing)
d.disable_motors()
