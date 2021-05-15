from graphics import *

def main():
    screenSetup()
    misterFrog()
    win.getMouse()
    win.close()


def screenSetup():
    # win = GraphWin("Frogger", 1000, 1000, autoflush=False)
    # win.setBackground("black")
    # win.setCoords(0, 100, 100, 0)
    finishLine = Rectangle(Point(99, 100), Point(100, 0))
    finishLine.setFill("lime")
    finishLine.draw(win)

    line1 = Rectangle(Point(89, 100), Point(90, 0))
    line1.setFill("white")
    line1.draw(win)

    line2 = Rectangle(Point(79,100), Point(80, 0))
    line2.setFill("white")
    line2.draw(win)

    line3 = Rectangle(Point(69,100), Point(70, 0))
    line3.setFill("white")
    line3.draw(win)

    line4 = Rectangle(Point(59,100), Point(60, 0))
    line4.setFill("white")
    line4.draw(win)

    line5 = Rectangle(Point(49,100), Point(50, 0))
    line5.setFill("white")
    line5.draw(win)

def misterFrog():
    froggo = Image(Point(40, 50), "senor_froggo.png")
    froggo.draw(win)

# def objectSetup():
#   same structure as screenSetup() but for obstacle elements


# def frogMover(**takes frog as arguement**):
#   structure that takes last pressed key and acts accordingly
#   ex.
#       if(key is left):
#           move frog left
#           break
#       if(key is right):
#           move frog right
#           break


win = GraphWin("Frogger", 1000, 1000, autoflush=False)
win.setBackground("black")
win.setCoords(0, 100, 100, 0)
main()