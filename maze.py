from line import *
import time
from window import Window
import random

# Line intentionally left blank

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed = None):
        self.x1, self.y1, self.num_rows, self.num_cols = x1, y1, num_rows, num_cols
        self.cell_size_x, self.cell_size_y, self.win = cell_size_x, cell_size_y, win
        if seed != None:
            random.seed(seed)
        else:
            random.seed()
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(0, self.num_cols):
            column = []
            x1 = self.x1 + (i * self.cell_size_x)
            x2 = x1 + self.cell_size_x

            for j in range(0, self.num_rows):
                y1 = self.y1 + (j * self.cell_size_y)
                y2 = y1 + self.cell_size_y

                point1 = Point(x1, y1)
                point2 = Point(x2, y2)

                column.append(Cell(point1, point2, self.win))

            self._cells.append(column)
        
        for col_index, pillar in enumerate(self._cells):
            for row_index, block in enumerate(pillar):
                self._draw_cell(col_index, row_index)

    def _draw_cell(self, i, j):
        #cell_x = self.x1 + (i * self.cell_size_x)
        #cell_y = self.y1 + (j * self.cell_size_y)
        cell = self._cells[i][j]
        cell.draw()
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrace_and_exit(self):
        self._cells[0][0].has_top_wall = False
        #print(f"Top wall of entrance after modification: {self._cells[0][0].has_top_wall}")
        self._cells[-1][-1].has_bottom_wall = False
        #print(f"Bottom wall of exit after modification: {self._cells[-1][-1].has_bottom_wall}")
        self._cells[0][0].draw()
        #print("Entrance Broken")
        self._cells[-1][-1].draw()
        #print("Exit Broken")
        self.win.redraw()
