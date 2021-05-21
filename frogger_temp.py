from graphics import *

def main():
    screenSetup()
    misterFrog()
    win.getMouse()
    win.close()


def screenSetup():
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
    froggo = Image(Point(44.5, 50), "senor_froggo.png")
    froggo.draw(win)
    game_loop(froggo)

# *************** beta function ***************
def game_loop(froggo):          
    while True:
        froggo_center = froggo.getAnchor()
        if(froggo_center.getX() < 90):
            frogMover(froggo)
            update()
        else:
            
            # level +=
            pass
# *************** beta function ***************

# def objectSetup():
#   same structure as screenSetup() but for obstacle elements


def frogMover(froggo):
    mover = win.checkKey()
    if(mover == 'Up'):
        froggo.move(0,-10)
    elif(mover == 'Down'):
        froggo.move(0,10)
    elif(mover == 'Right'):
        froggo.move(10,0)
    elif(mover == 'Left'):
        froggo.move(-10,0)
    elif(mover == 'x'):
        win.close
    else:
        pass


win = GraphWin("Frogger", 1000, 1000, autoflush=False)
win.setBackground("black")
win.setCoords(0, 100, 100, 0)
main()