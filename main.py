from window import Window
from line import *
from maze import Maze

# Line Intentionally Left Blank

def main():
    win = Window(800, 600)
    line1 = Line(Point(100, 100), Point(100, 200))
    line2= Line(Point(200, 200), Point(200, 300))
    #
    m1 = Maze(0, 0,)
    #
    win.wait_for_close()

main()