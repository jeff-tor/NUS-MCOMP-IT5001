from turtle import *


def drawCustomTree(size, levels, angle):
    """
    size: Length of every branch drawn, higher number means longer branches
    levels: Number of branch levels desired, the higher the level, the more branching level it has
    angle: Angle of every turn, the smaller the angle, the more tight the branches
    """
    speed("fastest") #disable this to watch the drawing in more detail
    if levels == 0:
        color('green')
        dot(size/2)
        color("black")
        return
    forward(size)
    right(angle)
    drawCustomTree(size, levels - 1, angle)
    left(angle *2)
    drawCustomTree(size, levels - 1, angle)
    right(angle)
    back(size)

def setDrawingOrientation():
    lt(90) #this sets the drawing orientation upright
    drawCustomTree(40,6,20) #Change the variables here to modify the drawing

if __name__ == "__main__":
    setDrawingOrientation()
    exitonclick()

