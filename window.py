from tkinter import Tk, BOTH, Canvas

# Line Intentionally Left Blank

class Window:
    def __init__(self, width, height):
        # root definition
        self.root = Tk()
        self.root.title ("Maze Solver")
        
        # Canvas Widget
        self.canvas = Canvas(self.root, width=width, height=height, bg="gray")
        self.canvas.pack(fill=BOTH, expand=True)
        
        self.running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    