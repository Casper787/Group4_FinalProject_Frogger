from graphics import *
import time

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

def misterFrog(truck, car, blueCar, pinkCar):
    froggo = Image(Point(44.5, 50), r'Images\senor_froggo.png')
    froggo.draw(win)
    game_loop(froggo, truck, car, blueCar, pinkCar)

def Truck():
    truck = Image(Point(55, 50), r'Images\truck_image.png')
    truck.draw(win)
    return truck
    
def Car():
    car = Image(Point(75, 35), r'Images\car_image.png')
    car.draw(win)
    return car
    
def PinkCar():
    pinkCar = Image(Point(85, 50), r'Images\pinkCarDown_image.png')
    pinkCar.draw(win)
    return pinkCar
    

def BlueCar():
    blueCar = Image(Point(65, 20), r'Images\blueCarDown_image.png')
    blueCar.draw(win)
    return blueCar
    

def car_move(froggo, truck, temp1, temp2, temp3):
    time.sleep(0.10)                # Every 0.10 seconds, move images
    truck.move(0,10)                # Y coordinate = speed of movement
    temp_center = truck.getAnchor()
    temp1_center = temp1.getAnchor()
    temp2_center = temp2.getAnchor()
    temp3_center = temp3.getAnchor()
    die_froggo(froggo, truck)       # Only 1 vehicle until it works, then slowly input the rest
    if(temp_center.getY() > 120):   # If vehicle is out of frame  
        truck.move(0, -130)         # Move to the opposite side of the frame
    temp1.move(0,-27)
    if(temp1_center.getY() < -10):
        temp1.move(0, 160)
    temp2.move(0,-5)
    if(temp2_center.getY() < -5):
       temp2.move(0, 115)
    temp3.move(0,7)
    if(temp3_center.getY() > 106):
        temp3.move(0, -107)

def die_froggo(froggo, truck):
    froggo_center = froggo.getAnchor()
    froggo_hitbox = ######
    truck_center = truck.getAnchor()
    truck_hitbox = #######
    print(truck_center)                             #For debugging purposes
    print(truck_hitbox)                             #For debugging purposes
    if(truck_hitbox.getCenter().getAnchor() > 120): #Same algorithm as line 64,65, to keep algorithm with the object
        truck_hitbox.move(0, -130)
    if(truck_hitbox.getCenter().getY() == froggo_hitbox.getCenter().getY() and truck_hitbox.getCenter().getX() == froggo_hitbox.getCenter().getX()):        #Wrong comparison. Should compare bottom Y coord of truck 
                                                                                                                                                            #and top Y coord of frog, if they overlap, move frog back
        froggo.move(-10, 0)

def frogMover(froggo):
    mover = win.checkKey()
    if(mover == 'Up'):
        froggo.move(0,-10)
    elif(mover == 'Down'):
        froggo.move(0,10)
    elif(mover == 'Right'):
        froggo.move(10,0)
        print(froggo)           #For debugging purposes. To know where the frog's center lands
    elif(mover == 'Left'):
        froggo.move(-10,0)
    elif(mover == 'x'):
        win.close
    else:
        pass

win = GraphWin("Frogger", 1000, 1000, autoflush=False)
win.setBackground("black")
win.setCoords(0, 100, 100, 0)

def game_loop(froggo, truck, car, blueCar, pinkCar):          
    while True:
        froggo_center = froggo.getAnchor()
        frogMover(froggo)
        if(froggo_center.getX() < 100):
            temp = truck
            temp1 = car
            temp2 = blueCar
            temp3 = pinkCar
            car_move(froggo, temp, temp1, temp2, temp3)
            
            # level +=

def main():
    screenSetup()
    truck = Truck()
    car = Car()
    pinkCar = PinkCar()
    blueCar = BlueCar()
    misterFrog(truck, car, blueCar, pinkCar)
    win.getMouse()
    win.close()


if __name__ =="__main__":
    main()
