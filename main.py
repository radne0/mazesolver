from window import Window
from shapes import Point, Line

def main():
    my_win = Window(800,600,"Maze Solver")
    print("hello...")

    mylines = [   
        Line( Point(50,100), Point(200,200)),
        Line( Point(400,200), Point(200,600)),
        Line( Point(50,100), Point(200,400)),
        Line( Point(300,50), Point(400,100)),
        Line( Point(50,100), Point(300,450))
    ]

    colors = ["red","blue","black","green","orange"]
    for i,line in enumerate(mylines):
        my_win.draw_line(line,colors[i])
    my_win.wait_for_close()

main()