from window import Window
from shapes import Point, Line
from cell import Cell


def all_wall_types(my_win):

    all_cells = [
        Cell(50, 100, 50, 100, my_win,rw=False,lw=False,tw=False,bw=False),         
        Cell(50, 100, 150, 200, my_win,rw=False,lw=False,tw=False,bw=True), 
        Cell(50, 100, 250, 300, my_win,rw=False,lw=False,tw=True,bw=False), 
        Cell(50, 100, 350, 400, my_win,rw=False,lw=False,tw=True,bw=True),  
        Cell(150, 200, 50, 100, my_win,rw=False,lw=True,tw=False,bw=False), 
        Cell(150, 200, 150, 200, my_win,rw=False,lw=True,tw=False,bw=True),
        Cell(150, 200, 250, 300, my_win,rw=False,lw=True,tw=True,bw=False), 
        Cell(150, 200, 350, 400, my_win,rw=False,lw=True,tw=True,bw=True),
        Cell(250, 300, 50, 100, my_win,rw=True,lw=False,tw=False,bw=False),          
        Cell(250, 300, 150, 200, my_win,rw=True,lw=False,tw=False,bw=True), 
        Cell(250, 300, 250, 300, my_win,rw=True,lw=False,tw=True,bw=False), 
        Cell(250, 300, 350, 400, my_win,rw=True,lw=False,tw=True,bw=True),  
        Cell(350, 400, 50, 100, my_win,rw=True,lw=True,tw=False,bw=False), 
        Cell(350, 400, 150, 200, my_win,rw=True,lw=True,tw=False,bw=True),
        Cell(350, 400, 250, 300, my_win,rw=True,lw=True,tw=True,bw=False), 
        Cell(350, 400, 350, 400, my_win)
    ]

    for cell in all_cells:
        cell.draw()




def main():
    my_win = Window(800,600,"Maze Solver")
    all_wall_types(my_win)
    my_win.wait_for_close()

main()