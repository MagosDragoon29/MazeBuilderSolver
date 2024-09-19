from tkinter import Tk, BOTH, Canvas

# Line Intentionally Left Blank

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y




class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)




class Cell:
    def __init__(self, point1, point2, window):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window

    def draw(self):
        if self.has_left_wall:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(self._win.canvas, 'black')
        if self.has_right_wall:
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(self._win.canvas, 'black')
        if self.has_top_wall:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(self._win.canvas, 'black')
        if self.has_bottom_wall:
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(self._win.canvas, 'black')
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            color = 'gray'
        else:
            color = 'red'
        start_point = Point((self._x1 + self._x2) /2, (self._y1 + self._y2) /2)
        end_point = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        Line(start_point, end_point).draw(self._win.canvas, color)