from window import Window
from line import *

# Line Intentionally Left Blank

def main():
    win = Window(800, 600)
    line1 = Line(Point(100, 100), Point(100, 200))
    line2= Line(Point(200, 200), Point(200, 300))
    #
    point1 = Point(100, 100)
    point2 = Point(200, 200)
    cell1 = Cell(point1, point2, win)
    cell1.draw()
    #
    win.wait_for_close()

main()