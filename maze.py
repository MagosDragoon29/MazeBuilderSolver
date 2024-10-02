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
            self.seed = seed
        else:
            random.seed()
            self.seed = None

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
        time.sleep(0.001)

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

    def _reset_cells_visited(self):
        for pillar in self._cells:
            for block in pillar:
                block.visited = False

    def _break_walls_r(self, i, j):
        # i is column, j is row
        current_cell = self._cells[i][j]
        current_cell.visited = True
        looping = True
        if i == 0:
            left = None
        else:
            left = self._cells[i-1][j]
        if i == len(self._cells) - 1:
            right = None
        else:
            right = self._cells[i+1][j]
        if j == 0:
            top = None
        else: 
            top = self._cells[i][j-1]
        if j == len(self._cells[i]) - 1:
            bottom = None
        else:
            bottom = self._cells[i][j+1]
        
        while looping:
            to_visit = []
            if left and not left.visited:
                to_visit.append(("left", left))
            if right and not right.visited:
                to_visit.append(("right", right))
            if top and not top.visited:
                to_visit.append(("top", top))
            if bottom and not bottom.visited:
                to_visit.append(("bottom", bottom))
            if not to_visit:
                current_cell.draw()
                return
            
            direction, next_cell = random.choice(to_visit)
            
            if direction == "left":
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
                self._break_walls_r(i-1, j)
            elif direction == "right":
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
                self._break_walls_r(i+1, j)
            elif direction == "top":
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                self._break_walls_r(i, j-1)
            elif direction == "bottom":
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
                self._break_walls_r(i, j+1)
        self._reset_cells_visited()

    def solve(self):
        self._reset_cells_visited()
        solved = self._solve_r(0,0)
        return solved 

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if i == len(self._cells)-1 and j == len(self._cells[i]) -1:
            print("Exit found!")

        if i == len(self._cells)-1 and j == len(self._cells[i]) -1:
            return True
        if i == 0:
            left = None
        else:
            left = self._cells[i-1][j]
        if i == len(self._cells) - 1:
            right = None
        else:
            right = self._cells[i+1][j]
        if j == 0:
            top = None
        else: 
            top = self._cells[i][j-1]
        if j == len(self._cells[i]) - 1:
            bottom = None
        else:
            bottom = self._cells[i][j+1]

        #print(f"Current cell: {i}, {j}")
        #print(f"Top: {top is not None}, Bottom: {bottom is not None}, Left: {left is not None}, Right: {right is not None}")
        #print(f"Current cell walls: top={current_cell.has_top_wall}, bottom={current_cell.has_bottom_wall}, left={current_cell.has_left_wall}, right={current_cell.has_right_wall}")

        #if top:
            #print(f"Top cell visited: {top.visited}, Wall broken: {not current_cell.has_top_wall}")
        if top and not top.visited and not current_cell.has_top_wall:
            #print(f"attempting move from cell: {i}, {j} to cell: {i}, {j-1}")
            current_cell.draw_move(top)
            if self._solve_r(i, j-1):
                return True
            else:
                current_cell.draw_move(top, undo=True)

        #if bottom:
            #print(f"Bottom cell visisted: {bottom.visited}, wall broken: {not current_cell.has_bottom_wall}")        
        if bottom and not bottom.visited and not current_cell.has_bottom_wall:
            #print(f"attempting move from cell: {i}, {j} to cell: {i}, {j+1}")
            current_cell.draw_move(bottom)
            if self._solve_r(i, j+1):
                return True
            else:
                current_cell.draw_move(bottom, undo=True)

        #if left:
            #print(f"Left cell visisted: {left.visited}, wall broken: {not current_cell.has_left_wall}")      
        if left and not left.visited and not current_cell.has_left_wall:
            #print(f"attempting move from cell: {i}, {j} to cell: {i-1}, {j}")
            current_cell.draw_move(left)
            if self._solve_r(i-1, j):
                return True
            else:
                current_cell.draw_move(left, undo=True)

        #if right:
            #print(f"Right cell visisted: {right.visited}, wall broken: {not current_cell.has_right_wall}")  
        if right and not right.visited and not current_cell.has_right_wall:
            #print(f"attempting move from cell: {i}, {j} to cell: {i+1}, {j}")
            current_cell.draw_move(right)
            if self._solve_r(i+1, j):
                return True
            else:
                current_cell.draw_move(right, undo=True)
        return False