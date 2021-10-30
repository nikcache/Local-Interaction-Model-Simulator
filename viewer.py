#Importing Modules
from Block import *
from Grid import *
from graphics import *
from Button import *

#Creating Grid
def makeGrid(vwin, Size, numThings, objType):

    #setting coords for Grid Window
    vwin.setCoords(-1, Size + 2, Size, -3)
    return Grid(vwin,0,0, Size,Size,1,1, numThings, objType)
    
#Function for grid window
def viewPopulation(currentType):
    
    #Setting up initial variables

    #Grid size
    Size = 4

    #the number of occupied spots in the grid
    numThings = len(currentType.getLowerList()) - 1

    #declaring the type of structure it is (i.e. City)
    #getType("down") returns what's below the structure [currentType] (i.e. Neighborhoods)
    objType = currentType.getType("down").upper()
    
    #Creating Window
    win = GraphWin("Test Window", 600, 1000)
    win.setBackground("#8C93A8")

    #Creating an instance of the grid
    g = makeGrid(win, Size, numThings, objType)

    #Creating buttons
    backButton = Button(win, Point(0, -1.75), 1, 1, "Back", 26)
    quitButton = Button(win, Point(1.5, 4.75), 4, 1, "Quit", 26)

    #Directory location
    basePath = currentType.getType("here").upper() + ":/"
    extPath = ""
    
    #Dynamic Text
    #Title Text
    dirTitle = Text(Point(1, -2), "Path: ")
    dirTitle.setSize(18)
    dirTitle.draw(win)
    
    dirText = Text(Point(2, -1.75), basePath)
    dirText.setSize(16)
    dirText.draw(win)

    #Starting with the right colors
    try:
            
        buttonList = []
        
        for buttonlist in g.buttonMatrix:
            for button in buttonlist:
                buttonList.append(button)

        #counter
        i = 0

        for thing, obj in currentType.getLowerList().items():
            buttonList[i].setColor(returnColor(obj.getCharacter()))

            #incrementing counter
            i = i + 1

        currentType.getCity().simulate = False
                     
    except:
        pass

    #setting person view to false
    pView = False

    try:
        pt = win.getMouse()
    except:
        return
    
    while not quitButton.clicked(pt):

        try:
            #Traversing through the list of grid spaces
            for buttonlist in g.buttonMatrix:
                for button in buttonlist:
                    if button.clicked(pt):
                         #print(g.getClickPos(pt))
                        g.undrawAll()
                        tempIn = button.getLabel()[1:]
                        extPath = extPath + button.getLabel() + "/"

                        #deleting instance of grid
                        del g

                        if currentType.getType("down") != "p":
                           
                            #Redefining currentType
                            currentType = currentType.getLowerList()[currentType.getType("down") + str(tempIn)]
                            g = makeGrid(win, Size, len(currentType.getLowerList()) - 1, currentType.getType("down"))

                        else:
                            pView = True
                            pCurr = currentType.getLowerList()[currentType.getType("down") + str(tempIn)]

                            tempfriendList = ""
                            
                            for friend in pCurr.friends:
                                tempfriendList = tempfriendList + friend.character.capitalize()\
                                                 + "-" + friend.social.capitalize() + " [" +str(friend.getiPayoff()) + "]\n"

                            #UI Elements
                            #Design Elements 
                            rect1 = Rectangle(Point(0, -1), Point(3, 3))
                            rect1.setFill("#B5C2B7")
                            rect1.draw(win)
                            
                            #Text elements
                            fText = Text(Point(1.5, 1), "Type: " + (pCurr.getCharacter()).capitalize() + " [" + str(pCurr.getiPayoff()) + "]" +\
                                                                     "\n\n Social: " + (pCurr.getSocial()).capitalize() +\
                                                                     "\n\n Friend List:                \n\n" + \
                                                                     str(tempfriendList))
                            fText.setSize(18)
                            fText.draw(win)
                                
        except:
            pass
        
        if backButton.clicked(pt):
            if (len(basePath) + len(extPath)) > 3:
                try:
                    #deleting the instance of the grid
                    g.undrawAll()
                    del g
                except:
                    pass

                try:
                    fText.undraw()
                    rect1.undraw()
                except:
                    pass

                extPath = extPath[:-3]
                if currentType.getType("here") == "f" and pView:
                    pView = False
                else:
                    currentType = currentType.getUpper()
                g = makeGrid(win, Size, len(currentType.getLowerList()) - 1, currentType.getType("down"))

        #Updating colors
        try:
            
            #List of all grid slots
            buttonList = []
            
            for buttonlist in g.buttonMatrix:
                for button in buttonlist:
                    buttonList.append(button)

            #counter
            i = 0

            for thing, obj in currentType.getLowerList().items():
                buttonList[i].setColor(returnColor(obj.getCharacter()))

                #incrementing counter
                i = i + 1
                     
        except:
            pass

        dirText.setText(basePath + extPath)

        try:
            pt = win.getMouse()
        except:
            return
    try:
        win.close()
    except:
        return

#Function used to determine color of grid spaces  
def returnColor(char):
    if char == "altruist":
        return "green"
    elif char == "egoist":
        return "blue"
    elif char == "hooligan":
        return "red"

