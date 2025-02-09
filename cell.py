from shapes import Line, Point
#Grid / Cell class

class Cell:
    def __init__(self,x1,x2,y1,y2,win,lw=True,rw=True,tw=True,bw=True):
        self.has_left_wall = lw
        self.has_right_wall = rw
        self.has_top_wall = tw
        self.has_bottom_wall = bw
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        
    def draw(self):
        if self.has_left_wall: 
            self._win.draw_line(Line( Point(self._x1,self._y1), Point(self._x1,self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line( Point(self._x2,self._y1), Point(self._x2,self._y2)))
        if self.has_top_wall: 
            self._win.draw_line(Line( Point(self._x1,self._y1), Point(self._x2,self._y1)))
        if self.has_bottom_wall: 
            self._win.draw_line(Line( Point(self._x1,self._y2), Point(self._x2,self._y2)))


