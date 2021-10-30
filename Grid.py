#Importing Modules
from graphics import *

#Defining Grid Class
class gridButton:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = gridButton(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("lightgrey")
        self.rect.setWidth(2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setSize(26)
        self.label.setFill("white")
        self.label.setStyle("bold")
        self.label.draw(win)
        self.active = True
        #self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        #print("clicked", p.getX(), p.getY(), self.xmin, self.xmax)
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self, color):
        "Sets this button to 'inactive'."
        self.setColor(color)
        self.label.setFill('black')
        self.rect.setWidth(1)
        self.active = False

    def setColor(self,color):
        self.rect.setFill(color)

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()
        del self
  
class Grid:
    """A grid of squares/buttons"""
    def __init__(self, win, startX, startY, numCols, numRows, squareWidth, squareHeight, numSlots, objType):
        """initializes a 2D list of blank button objects"""
        self.buttonMatrix = []
        self.numRows = numRows
        self.numCols = numCols
        
        i = 0

        for y in range(startY,numRows):
            row = []
            for x in range(startX,numCols):
                if numSlots >= i:
                    button = gridButton(win,Point(x,y),1,1,(objType.upper() + str(i)))
                    row.append(button)
                else:
                    button = gridButton(win,Point(x,y),1,1,("--"))
                    button.deactivate("darkgrey")
                    row.append(button)
                i = i + 1

            self.buttonMatrix.append(row)
    
    def getMatrix(self):
        return self.buttonMatrix
                
    def getClickPos(self, clickPt):
        x = clickPt.getX()
        y = clickPt.getY()

        return round(y), round(x)
        """returns the column and row number of the button that was clicked
           assumes the point clickPt is in/on the grid"""

    def setSquareColor(self, y, x, color):
        self.buttonMatrix[y][x].setColor(color)

    def setRowColor(self, rowNum,color):
        for c in range(self.numCols):
            self.buttonMatrix[rowNum][c].setColor(color)

    def setColColor(self, colNum,color):
        for r in range(self.numRows):
            self.buttonMatrix[r][colNum].setColor(color)

    def undrawAll(self):
        for buttonlist in self.buttonMatrix:
            for button in buttonlist:
                button.undraw()

 
def main():
    Size = 10
    
    #create the application window
    win = GraphWin("Fun with 2D lists", 600, 600)
 
    win.setCoords(-3, -3, Size + 2, Size + 2)
    

    ##add code here that creates a quitButton
    
    quitBut = gridButton(win,Point(20,20),2,1,"quit")

    #fill in the constructor for the Grid class above and then use it to create a Grid object here
    g = Grid(win,0,0, Size,Size,1,1)
 
    pt = win.getMouse()

    ##add a while loop here that will keep taking mouse clicks until the quit button is clicked

    while not quitBut.clicked(pt):

        y,x = g.getClickPos(pt)
        try:
            g.setSquareColor(y, x, "black")
            print(g.getClickPos(pt))
        except:
            print("Invalid Click")
        pt = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()


