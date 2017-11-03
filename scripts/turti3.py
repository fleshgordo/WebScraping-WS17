import Tkinter,turtle,time,random
from canvasvg import *

def saveImg():
    name = random.randint(1000,9999)
    backg = ninja.screen.bgcolor()
    r = round(backg[0]*255)
    g = round(backg[1]*255)
    b = round(backg[2]*255)
    nameSav = "svg/"+ str(r) + "_" + str(g) + "_" + str(b) + ".svg"
    ts = ninja.getscreen().getcanvas()
    canvasvg.saveall(nameSav, ts)
    print nameSav
    ninja.clear()

ninja = turtle.Turtle()
ninja.screen.title("bitbulla")
ninja.hideturtle()
#ninja.screen.bgpic("tmp/1.gif")
#ninja.screen.bgcolor("#abc123")
ninja.screen.screensize(900,500)
strich = 8
fill = 16
ninja.speed(1)

rgb = '#%02x%02x%02x' % (strich, (100+strich), 200)
rgbfill = '#%02x%02x%02x' % (fill,fill,fill)
ninja.pencolor(rgb);ninja.fillcolor(rgbfill)

ninja.penup()
ninja.setposition(0,0)
ninja.pendown()

def nachbar(xjetzt,yjetzt,allex,alley,schritt):
#http://stackoverflow.com/questions/32449670/trouble-when-using-coords-function-in-python-tkinter-canvas-to-modify-object-coo
    rando =  int(200)
    randr = int(400)
    randu =  int(-200)
    randl = int(-400)
    if round(xjetzt) > randr:
        stopx = 1
    elif round(xjetzt) < randl:
        stopx = 1
    else:
        stopx = 0
    if round(yjetzt) > rando:
        stopy = 1
    elif round(yjetzt) < randu:
        stopy = 1
    else:
        stopy = 0
    if xjetzt in allex:
        xindex = allex.index(xjetzt)
    else:
        xindex = int()
    if  alley[xindex] == yjetzt:
        rgb = '#%02x%02x%02x' % (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        rgbfill = '#%02x%02x%02x' % (fill,fill,fill)
        ninja.pencolor(rgb);ninja.fillcolor(rgbfill)
        print("achtung!")
    if yjetzt in alley:
        yindex = alley.index(yjetzt)
    else:
        yindex = int()
    if  allex[yindex] == xjetzt:
        rgb = '#%02x%02x%02x' % (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        rgbfill = '#%02x%02x%02x' % (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        ninja.pencolor(rgb);ninja.fillcolor(rgbfill)
        print("achtung!")
    if len(allex) > 75:
        stopx = 3
    if stopx + stopy >= 1:
#        ninja.screen.bgpic("tmp/2.gif")
        while positionx:
            positionx.pop(0)
        while positiony:
            positiony.pop(0)
        rgb1 = '#%02x%02x%02x' % (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        ninja.screen.bgcolor(rgb1)
        rgb = '#%02x%02x%02x' % (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        rgbfill = '#%02x%02x%02x' % (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        ninja.pencolor(rgb);ninja.fillcolor(rgbfill)
#       ninja.pensize(random.randint(1,20))
        stiftbreite = 20-(schritt[1]+1)
        ninja.pensize(stiftbreite)
        schritt[0] = random.randint(10,60)
        ninja.penup()
        ninja.setposition(0,0)
        ninja.pendown()
        time.sleep(3)
        neueRunde = schritt[1]
        if 2 < schritt[1] < 6:
            if schritt[1] == 1:
                ninja.begin_fill()
            else:
                ninja.end_fill()
                ninja.begin_fill()
        schritt[1] =  neueRunde + 1
        return schritt
    else:
        return schritt

def ziehen(ok):
    rundenTest = ok[1]
    print "RUNDE: " + str(rundenTest)
    if rundenTest >= 10:
        print("THE END")
        saveImg()
    else:
        schritte   = ok[0]
        if schritte > 25:
            hm = random.randint(0,10)
            if hm >=7 :
                ninja.rt(random.randint(1,180))
            elif hm == 4:
                ninja.lt(random.randint(1,180))
            xpo  = ninja.xcor()
            ypo  = ninja.ycor()
            positionx.append(round(xpo))
            positiony.append(round(ypo))
            ninja.fd(schritte)
            xpo_nach  = ninja.xcor()
            ypo_nach  = ninja.ycor()
            x = round(xpo_nach)
            y = round(ypo_nach)
            print "VON  X: " + str(round(xpo))
            print "VON  Y: " + str(round(ypo))
            print "NACH X: " + str(round(x))
            print "NACH Y: " + str(round(y))
            print positionx
            print positiony
            ziehen(nachbar(x,y,positionx,positiony,ok))
        else:
            hm = random.randint(0,10)
            schritte   = ok[0]
            if hm >= 7 :
                ninja.rt(90)
            elif hm == 4:
                ninja.lt(90)
            xpo  = ninja.xcor()
            print xpo
            ypo  = ninja.ycor()
            print ypo
            positionx.append(round(xpo))
            positiony.append(round(ypo))
            ninja.fd(schritte)
            time.sleep(0.25)
            xpo_nach  = ninja.xcor()
            ypo_nach  = ninja.ycor()
            x = round(xpo_nach)
            y = round(ypo_nach)
            print "VON  X: " + str(round(xpo))
            print "VON  Y: " + str(round(ypo))
            print "NACH X: " + str(round(x))
            print "NACH Y: " + str(round(y))
            print positionx
            print positiony
            ziehen(nachbar(x,y,positionx,positiony,ok))

positionx = []
positiony = []

for i in range(50):
    ninja.pensize(20)
    schritte = 80
    runden  = 1
    anfang = [0,0]
    anfang[0] = schritte
    anfang[1] = runden
    print anfang
    ziehen(anfang)
    time.sleep(5)
    print "NINJA ENDE NINJA START"

turtle.exitonclick()
