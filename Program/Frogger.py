from graphics import *

def main():
    screenSetup()
    Truck()
    Car()
    PinkCar()
    BlueCar()
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
    froggo = Image(Point(40, 50), r'Images\senor_froggo.png')
    froggo.draw(win)
    game_loop(froggo)

def Truck():
    truck = Image(Point(55, 50), r'Images\Truck_image.png')
    truck.draw(win)
    # truck = Image(Point(85,20),r'Images\Truck_image.png')
    # truck.draw(win)
    # truck = Image(Point(95,95),r'Images\Truck_image.png')
    # truck.draw(win)
    return truck
    
def Car():
    car = Image(Point(75, 35), r'Images\Car_image.png')
    car.draw(win)
    car = Image(Point(65, 80), r'Images\Truck_image.png')
    car.draw(win)
    car = Image(Point(95, 65), r'Images\CarDown_image.png')
    car.draw(win)
    
def PinkCar():
    pinkCar = Image(Point(85, 50), r'Images\PinkCarDown_image.png')
    pinkCar.draw(win)
    pinkCar = Image(Point(85, 80), r'Images\PinkCarDown_image.png')
    pinkCar.draw(win)
    pinkCar = Image(Point(65, 10), r'Images\PinkCarUp_image.png')
    pinkCar.draw(win)
    pinkCar = Image(Point(55, 95), r'Images\PinkCarDown_image.png')
    pinkCar.draw(win)
    

def BlueCar():
    blueCar = Image(Point(55, 20), r'Images\BlueCarDown_image.png')
    blueCar.draw(win)
    # blueCar = Image(Point(75, 65), r'Images\BlueCarUp_image.png')
    # blueCar.draw(win)
    # blueCar = Image(Point(95, 35),  r'Images\BluecarDown_image.png')
    # blueCar.draw(win)
    
# *************** beta function ***************

# *************** beta function ***************

def car_move(truck):
    truck.move(0, 25)
    

def frogMover(froggo):
    mover = win.checkKey()
    if(mover == 'Up'):
        froggo.move(0,-5)
    elif(mover == 'Down'):
        froggo.move(0,5)
    elif(mover == 'Right'):
        froggo.move(5,0)
    elif(mover == 'Left'):
        froggo.move(-5,0)
    elif(mover == 'x'):
        win.close
    else:
        pass

win = GraphWin("Frogger", 1000, 1000, autoflush=False)
win.setBackground("black")
win.setCoords(0, 100, 100, 0)

def game_loop(froggo):          
    while True:
        froggo_center = froggo.getAnchor()
        frogMover(froggo)
        if(froggo_center.getX() < 100):
            update(10)
            temp = Truck()
            car_move(temp)
            
            # level +=

def main():
    screenSetup()
    Car()
    PinkCar()
    BlueCar()
    misterFrog()
    win.getMouse()
    win.close()

if __name__ =="__main__":
    main()