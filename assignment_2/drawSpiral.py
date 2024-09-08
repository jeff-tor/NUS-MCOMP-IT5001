from turtle import *

def drawSpiral(line_length):

    shortest_line = 5
    adjacent_angle = 90
    if line_length < shortest_line:
        fd(line_length)
    else:
        while line_length >= shortest_line:
            fd(line_length)
            rt(adjacent_angle)
            line_length -= 5

if __name__ == "__main__":
    drawSpiral(100)