import unittest
from window import Window
from maze import Maze

# Line intentionally left blank

win = Window(800, 600)
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 30
        num_rows = 25
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        m1._break_entrace_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)
        win.redraw()
        m1._break_walls_r(0, 0)
        win.wait_for_close()
if __name__ == "__main__":
    unittest.main()