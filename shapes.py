# simple point class.
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

# simple line class
class Line:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    
    # draw the line on the canvas.
    def draw(self,canvas, fill_color="black"):
        canvas.create_line( self.p1.x,self.p1.y, self.p2.x,self.p2.y, fill=fill_color,width=2)



