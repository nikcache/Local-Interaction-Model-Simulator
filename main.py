#Main Program
#Nikesh, Kunal and Abi

from viewer import *
from graphics import *
from City import *
from txt import *
from Button import *
from makeLink import *

def mainApp():

    introWin()

def introWin():

    #Creating intro Window
    iwin = GraphWin("Intro Window", 400, 300)
    iwin.setCoords(0, 400, 400, 0)

    #UI elements
    
    #Text
    txt("Community Simulator", 200, 75, iwin, 20, "black", "bold")
    txt("By:                      \n\n Nikesh Ghimire\nKunal Sheth\n Abi Pradhan", 200, 200, iwin, 16, "black", "normal")

    #Buttons
    startButton = Button(iwin, Point(200, 325), 75, 50, "Start", 18)
    helpButton = Button(iwin, Point(125, 325), 50, 35, "Help", 14)
    helpButton.deactivate()
    quitButton = Button(iwin, Point(275, 325), 50, 35, "Quit", 14)
    
    
    #Mouse Click
    pt = iwin.getMouse()

    #Interaction
    while not quitButton.clicked(pt):

        if startButton.clicked(pt):
            iwin.close()
            simWin()
            break

        elif helpButton.clicked(pt):
            helpWin()

        try:            
            pt = iwin.getMouse()
        except:
            pass

    try:
        iwin.close()
    except:
        return
    
def helpWin():

    #Creating help window
    hwin = GraphWin("Help Window", 600, 600)
    hwin.setCoords(0, 600, 600, 0)

    #UI Elements

    #Text

    #Buttons
    closeButton = Button(hwin, Point(300, 550), 75, 50, "Close", 18)

    pt = hwin.getMouse()

    while not closeButton.clicked(pt):

        try:            
            pt = hwin.getMouse()
        except:
            pass

    try:
        hwin.close()
    except:
        pass

def simWin():

    swin = GraphWin("Simulation Settings", 800, 400)
    swin.setCoords(0, 400, 800, 0)

    #UI Elements

    #Design elements
    rect1 = Rectangle(Point(0, 0), Point(800, 100))
    rect1.setFill("#383838")
    rect1.setWidth(0)
    rect1.draw(swin)

    rect2 = Rectangle(Point(0, 0), Point(300, 405))
    rect2.setFill("#383838")
    rect2.setWidth(0)
    rect2.draw(swin)

    rect3 = Rectangle(Point(325, 325), Point(775, 375))
    rect3.setFill("#383838")
    rect3.draw(swin)

    #Divider
    div = Rectangle(Point(5, 98), Point(295, 102))
    div.setFill("white")
    div.draw(swin)

    #Divider
    div = Rectangle(Point(5, 148), Point(295, 153))
    div.setFill("white")
    div.draw(swin)

    #Divider
    div = Rectangle(Point(305, 148), Point(795, 152))
    div.setFill("#383838")
    div.draw(swin)
    
    #Static Text
    txt("Generate a Community!", 175, 50, swin, 20, "white", "bold")
    txt("Time:", 505, 50, swin, 20, "white", "bold")
    txt("Data Output", 150, 125, swin, 20, "white", "bold")
    txt("Population Count", 550, 125, swin, 20, "black", "bold")
    txt("C:", 340, 210, swin, 16, "black", "bold")
    txt("N:", 415, 210, swin, 16, "black", "bold")
    txt("B:", 490, 210, swin, 16, "black", "bold")
    txt("A:", 565, 210, swin, 16, "black", "bold")
    txt("F:", 640, 210, swin, 16, "black", "bold")
    txt("P:", 715, 210, swin, 16, "black", "bold")

    #Dynamic Text
    #Status Text
    statusText = Text(Point(550, 350), "Please click 'Generate' to continue")
    statusText.setFill("white")
    statusText.setSize(20)
    statusText.draw(swin)

    #Percentage Texts
    #Altruist Percentage
    aPerText = Text(Point(150, 180), "A: --.- %")
    aPerText.setFill("white")
    aPerText.setSize(20)
    aPerText.draw(swin)

    #Egoist Percentage
    ePerText = Text(Point(150, 260), "E: --.- %")
    ePerText.setFill("white")
    ePerText.setSize(20)
    ePerText.draw(swin)

    #Hooligan Percentage
    hPerText = Text(Point(150, 340), "H: --.- %")
    hPerText.setFill("white")
    hPerText.setSize(20)
    hPerText.draw(swin)

    #Simulation Tracker
    numSimText = Text(Point(150, 380), "Number of Sims: 0")
    numSimText.setFill("white")
    numSimText.setSize(14)
    numSimText.draw(swin)

    #Population Counters
    #City
    cCount = Text(Point(375, 210), "---")
    cCount.setSize(16)
    cCount.draw(swin)

    #Neighborhood
    nCount = Text(Point(450, 210), "---")
    nCount.setSize(16)
    nCount.draw(swin)

    #Blocks
    bCount = Text(Point(525, 210), "---")
    bCount.setSize(16)
    bCount.draw(swin)

    #Apartments
    aCount = Text(Point(600, 210), "---")
    aCount.setSize(16)
    aCount.draw(swin)

    #Families
    fCount = Text(Point(675, 210), "---")
    fCount.setSize(16)
    fCount.draw(swin)

    #People
    pCount = Text(Point(755, 210), "---")
    pCount.setSize(16)
    pCount.draw(swin)
    
    #Buttons
    genButton = Button(swin, Point(400, 50), 120, 35, "Generate", 18)
    simButton = Button(swin, Point(650, 50), 120, 35, "Simulate", 18)
        #Deactivating viewButton initially
    simButton.deactivate()
    quitButton = Button(swin, Point(750, 50), 60, 35, "Quit", 18)
    viewButton = Button(swin, Point(550, 290), 450, 50, "View Community", 18)
        #Deactivating viewButton initially
    viewButton.deactivate()

    #EntryBox
    numBox = Entry(Point(565, 50), 3)
    numBox.setFill("white")
    numBox.draw(swin)

    #Variables
    totalSim = 0

    pt = swin.getMouse()

    while not quitButton.clicked(pt):

        #If generate button is clicked
        if genButton.clicked(pt):
            statusText.setText("Generating...")
            comm = generate()
            links = establishLinks(comm)
            aPerText.setText("A: " + str(percentageData(comm)[0]) + " %")
            ePerText.setText("E: " + str(percentageData(comm)[1]) + " %")
            hPerText.setText("H: " + str(percentageData(comm)[2]) + " %")
            rect3.setFill("#a7feb8")
            statusText.setFill("#383838")

            #Updating Population Counters
            cCount.setText(str(1))
            nCount.setText(str(len(comm.getNeighborhoodList())))
            bCount.setText(str(len(comm.getBlockList())))
            aCount.setText(str(len(comm.getApartmentList())))
            fCount.setText(str(len(comm.getFamilyList())))
            pCount.setText(str(len(comm.getPersonList())))

            #Notifying completion of generating Community
            totalSim = 0
            numSimText.setText("Number of Sims: " + str(totalSim))
            statusText.setText("Community Generated!")
            viewButton.activate()
            simButton.activate()

        #If view button is clicked
        elif viewButton.clicked(pt):
            statusText.setText("Viewing Community...")
            comm.simulate = True
            viewPopulation(comm)
            statusText.setText("--------------------")

        #If simulate button is clicked
        elif simButton.clicked(pt):
            try:
                simNum = int(numBox.getText())
                totalSim = totalSim + simNum
                statusText.setText("Simulating...")
                percList = percentageData(comm)
                comm.simulate = True
                simulate(comm, simNum)
                comm.simulate = False
                    
                aPerText.setText("A: " + str(percentageData(comm)[0]) + " %")
                ePerText.setText("E: " + str(percentageData(comm)[1]) + " %")
                hPerText.setText("H: " + str(percentageData(comm)[2]) + " %")

                numSimText.setText("Number of Sims: " + str(totalSim))               
                statusText.setText("Successfully Simulated!")
            except:
                pass
            
        try:            
            pt = swin.getMouse()
        except:
            return

    try:
        swin.close()
    except:
        return

def generate():

    commBlock = City()
    return commBlock

def simulate(comm, num):

    for i in range(num):
        setPayOffRound(comm)
        setNextRoundChar(comm)
    
mainApp()

    
