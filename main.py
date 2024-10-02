from window import Window
from line import *
from maze import Maze
import time
import sys

# Line Intentionally Left Blank

def main():
    win = Window(800, 600)
    sys.setrecursionlimit(2000)
    #
    num_cols = 50
    num_rows = 50
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win, seed = 29)
    #
    m1._break_entrace_and_exit()
    m1._break_walls_r(0,0)
    time.sleep(2)
    solved = m1.solve()
    win.redraw()
    win.wait_for_close()

main()