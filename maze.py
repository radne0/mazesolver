import time
from cell import Cell

class Maze:
    def __init__(self,x1,y1, num_rows,num_cols, cell_size_x,cell_size_y,win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y 
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            row_cell = []
            for j in range(self.num_rows):
                new_cell = Cell(i,i,j,j,self.win)      # will fix this position in the draw cell call.
                row_cell.append(new_cell)
            self._cells.append(row_cell)

        for i in range(self.num_cols): 
            for j in range(self.num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        x_pos = self.x1 + self.cell_size_x*i
        y_pos = self.y1 + self.cell_size_y*j
        self._cells[i][j].x1 = x_pos
        self._cells[i][j].x2 = x_pos + self.cell_size_x
        self._cells[i][j].y1 = y_pos 
        self._cells[i][j].y2 = y_pos + self.cell_size_y
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    