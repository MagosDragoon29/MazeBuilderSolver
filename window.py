from tkinter import Tk, BOTH, Canvas

# Line Intentionally Left Blank

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title ("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height, bg="gray")
        self.canvas.pack(fill=BOTH, expand=True)
    