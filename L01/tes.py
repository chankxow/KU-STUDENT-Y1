from turtle import *

def drawlogs(size):
    pensize(size)
    pencolor('green')
    left(90)
    forward(200)
    left(70)
    bgcolor('grey')
    speed(0)

def drawCirclein(radius):
    pensize(2)
    forward(10)
    for i in range(10):
        pencolor('yellow')
        circle(radius)
        radius=radius-2
def drawDesignin():
    for i in range(10):
        drawCirclein(10)
        right(36)

def drawCircle(radius):
    pensize(2)
    forward(10)
    for i in range(6):
        pencolor('red')
        circle(radius)
        radius=radius-2
def drawDesign():
    for i in range(10):
        drawCircle(25)
        right(36)


drawlogs(5)
drawDesign()
drawDesignin()
done()