from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width, height,title="No Title"):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.title(title)
        self.canvas = Canvas(self.root,width=self.width,height=self.height,bg="blue")
        self.canvas.pack(fill=BOTH,expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW",self.close)        

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()

    def close(self):
        self.running = False
