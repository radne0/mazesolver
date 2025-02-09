from tkinter import Tk, BOTH, Canvas
from shapes import Point, Line

class Window:
    def __init__(self,width, height,title="No Title"):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.title(title)
        self.canvas = Canvas(self.root,width=self.width,height=self.height)
        self.canvas.pack(fill=BOTH,expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW",self.close)        

    # wait for button presses.  update windows etc...
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    # keeps redrawing window until running status changes.
    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()

    # This runs when X button is clicked currently.  (result: wait for close loop ends.)
    def close(self):
        self.running = False

    # Draw a line on the canvas.
    def draw_line(self,line,fill_color="black"):
        line.draw(self.canvas,fill_color)


