from window import Window
from shapes import Point, Line
from cell import Cell

def some_path(my_win):
    path =[
         Cell(500,550,50,100,my_win,tw=True,bw=False,lw=True,rw=True),
         Cell(500,550,100,150,my_win,tw=False,lw=True,rw=True,bw=False),
         Cell(500,550,150,200,my_win,tw=False,lw=True,rw=True,bw=False),
         Cell(500,550,200,250,my_win,tw=False,lw=True,rw=True,bw=False),
         Cell(500,550,250,300,my_win,tw=False,lw=True,rw=False,bw=True),
         Cell(550,600,250,300,my_win,tw=True,lw=False,rw=False,bw=True),
         Cell(600,650,250,300,my_win,tw=True,lw=False,rw=False,bw=True),
         Cell(650,700,250,300,my_win,tw=False,lw=False,rw=True,bw=True),
         Cell(650,700,200,250,my_win,tw=False,lw=True,rw=True,bw=False),
    ]



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

    for line in path:
        line.draw()


def main():
    my_win = Window(800,600,"Maze Solver")
    all_wall_types(my_win)
    some_path(my_win)
    my_win.wait_for_close()

main()