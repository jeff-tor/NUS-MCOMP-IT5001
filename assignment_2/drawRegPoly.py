from turtle import *

def drawRegPoly(l,n):
    angle_to_turn = 360/n
    for i in range (0,n):
        rt(angle_to_turn)
        fd(l)
    return 0

if __name__ == "__main__":
    drawRegPoly(100,8)