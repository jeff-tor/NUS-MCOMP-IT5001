from turtle import *

def drawFlower(l,p,n):
    polygon_angle = 360/p
    flower_angles = 360/n

    for i in range(0,n):
        lt(flower_angles)

        for i in range(0,p):
            lt(polygon_angle)
            fd(l)
    return 0


if __name__ == "__main__":
    drawFlower(100,8,10)