from graphics import *
import time

# Game lanes
def screenSetup(win):
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

# Game frog 
def misterFrog(truck, car, blueCar, pinkCar, win, level):
    froggo = Image(Point(44.5, 50), r'Images\senor_froggo.png')
    froggo.draw(win)
    game_loop(froggo, truck, car, blueCar, pinkCar, win, level)
# Game truck
def Truck(win):
    truck = Image(Point(54.5, 50), r'Images\truck_image.png')
    truck.draw(win)
    return truck
# Game red car
def Car(win):
    car = Image(Point(74.5, 30), r'Images\car_image.png')
    car.draw(win)
    return car
# Game pink car  
def PinkCar(win):
    pinkCar = Image(Point(84.5, 40), r'Images\pinkCarDown_image.png')
    pinkCar.draw(win)
    return pinkCar
# Game blue car
def BlueCar(win):
    blueCar = Image(Point(64.5, 20), r'Images\blueCarUp_image.png')
    blueCar.draw(win)
    return blueCar

# Moves cars in the Y direction
# If car goes out of frame, moves the car to the opposite side of the frame
# Creates the teleportation illusion reminiscent of Pac-man
def car_move(froggo, truck, car, blue_car, pink_car, win, level):
    time.sleep(0.05)                         # Every 0.05 seconds, vehicles will move, animation is smoother with this amount of seconds
    truck_center = truck.getAnchor()
    car_center = car.getAnchor()
    blue_car_center = blue_car.getAnchor()
    pink_car_center = pink_car.getAnchor()                                  
    truck.move(0, 5 * level)                                                
    if(truck_center.getY() > 120):           # Verifies if vehicle is out of frame
        truck.move(0, -130)                  # When TRUE, vehicle is moved to opposite side of frame
    car.move(0,-5 * level)
    if(car_center.getY() < -10):
        car.move(0, 160)
    blue_car.move(0,-5.0 * level)
    if(blue_car_center.getY() < -15):
        blue_car.move(0, 115)
    pink_car.move(0, 10 * level)
    if(pink_car_center.getY() > 110):
        pink_car.move(0, -120)
    collision(froggo, truck, car, blue_car, pink_car, win, level)       # Checks if frog and a vehicle have crashed


def win_or_lose(cond, win, level):  # Verifies if user has won or lost and shows appropriate screen
    # User has lost if the condition sent is an 'L' 
    # Loss message is illustrated
    # Buttons generated are "Quit" and "Play Again"
    if(cond == 'L'):
        win2 = GraphWin("Game Over", 300, 300)
        message = "YOU LOST :( "
        play_again_label = Text(Point(230, 270), "PLAY AGAIN")
        win2.setBackground("black")
        text = Text(Point(150, 150), message)
        text.setTextColor("white")
        text.setSize(30)
        text.setStyle("bold")
        text.draw(win2)
        # Play again button
        play_again = Rectangle(Point(175, 255), Point(285, 285))
        play_again.setWidth(3)
        play_again.setOutline("white")
        play_again.draw(win2)

        play_again_label.setStyle("bold")
        play_again_label.setTextColor("white")
        play_again_label.draw(win2)

    # User has lost if the condition sent is an 'W' 
    # Win message is illustrated
    # Buttons generated are "Quit" and "Next Level"
    elif(cond == 'W'):
        win2 = GraphWin("GG", 300, 300)
        message = "YOU WON :) "
        next_level_label = Text(Point(230, 270), "NEXT LEVEL")
        win2.setBackground("black")
        text = Text(Point(150, 150), message)
        text.setTextColor("white")
        text.setSize(30)
        text.setStyle("bold")
        text.draw(win2)
        # Next level button
        next_level = Rectangle(Point(175, 255), Point(285, 285))
        next_level.setWidth(3)
        next_level.setOutline("white")
        next_level.draw(win2)

        next_level_label.setStyle("bold")
        next_level_label.setTextColor("white")
        next_level_label.draw(win2)

    # Quit game button
    quitGame = Rectangle(Point(15, 255), Point(65, 285))
    quitGame.setWidth(3)
    quitGame.setOutline("white")
    quitGame.draw(win2)
    
    quitGameLabel = Text(Point(40, 270), "QUIT")
    quitGameLabel.setStyle("bold")
    quitGameLabel.setTextColor("white")
    quitGameLabel.draw(win2)

    # If the player choses to play again the page will close and another
    # game will start and if he chooses to quit the window will close
    click = win2.getMouse()
    if(click.getX() >= 175 and click.getX() <= 285 and click.getY() >= 255 and click.getY() <= 285):
        win2.close()
        win.close()
        if(cond == 'W'):
            main(level + 1) 
        else:
            main(level)                 
    if(click.getX() >= 15 and click.getX() <= 65 and click.getY() >= 255 and click.getY() <= 285):
        win.close()  
    for i in range(300):
        time.sleep(1)
        if(click.getX() < 150):
            win2.close()  
            pass                        #If user clicks quit, show game over screen
                                        #If user clicks play again, call main()

# Will check for intersections between the frog and any vehicle
# If an intersection is found
# User has lost game and lose screen is initialized
def collision(froggo, truck, car, blueCar,  pinkCar, win, level):
    froggo_center = froggo.getAnchor()
    truck_center = truck.getAnchor()
    car_center = car.getAnchor()
    pinkCar_center = pinkCar.getAnchor()
    blueCar_center = blueCar.getAnchor()
    
    if(truck_hit(froggo_center, truck_center) or car_hit(froggo_center, car_center) or pinkCar_hit(froggo_center, pinkCar_center) or blueCar_hit(froggo_center, blueCar_center)):
        win_or_lose('L', win, level)        # Parameter 'L' has been passed meaning user has lost, loss screen is initialized
    else:
        pass
# Will detect if the frog and the truck intersect
def truck_hit(froggo, truck):
    if(froggo.getY() >= truck.getY() - 10 and froggo.getY() <= truck.getY() + 10 and froggo.getX() == truck.getX()):
        return True
    else:
        return False
# Will detect if the frog and the red car intersect
def car_hit(froggo, car):
    if(froggo.getY() >= car.getY() - 1 and froggo.getY() <= car.getY() + 1 and froggo.getX() == car.getX()):
        return True
    else:
        return False
# Will detect if the frog and the pink car intersect
def pinkCar_hit(froggo, pinkCar):
    if(froggo.getY() == pinkCar.getY() and froggo.getX() == pinkCar.getX()):
        return True
    else:
        return False
# Will detect if the frog and the blue car intersect
def blueCar_hit(froggo, blueCar):
    if(froggo.getY() == blueCar.getY() - 5 and froggo.getX() == blueCar.getX()):
        return True
    else:
        return False

# Allows user to move frog with keyboard arrow keys
def frogMover(froggo, win):
    mover = win.checkKey()
    if(mover == 'Up'):
        froggo.move(0,-10)
    elif(mover == 'Down'):
        froggo.move(0,10)
    elif(mover == 'Right'):
        froggo.move(10,0)
    elif(mover == 'Left'):
        froggo.move(-10,0)
    else:
        pass
# Main loop that will keep the game running until game has ended by user
def game_loop(froggo, truck, car, blueCar, pinkCar, win, level):
    while True:
        froggo_center = froggo.getAnchor()
        frogMover(froggo, win)
        if(froggo_center.getX() < 94.5):        # Ensures frog is to the left of the finish line                                   
            temp = truck                        
            temp1 = car
            temp2 = blueCar
            temp3 = pinkCar
            car_move(froggo, temp, temp1, temp2, temp3, win, level)         
        elif(froggo_center.getX() == 94.5):     # Frog has reached finish line
            (win_or_lose('W', win, level))      # Parameter 'W' has been sent meaning player has won, win screen is initialized

def main(level):
    win = GraphWin("Frogger", 1000, 1000, autoflush=False)      # Game screen initiation
    win.setBackground("black")
    win.setCoords(0, 100, 100, 0)
    screenSetup(win)                                            # Initializes screen lanes
    truck = Truck(win)                                          # Vehicle functions return the vehicle
    car = Car(win)                                              # Vehicles are stored in a variable for easier 
    pinkCar = PinkCar(win)                                      #   management through functions
    blueCar = BlueCar(win)
    misterFrog(truck, car, blueCar, pinkCar, win, level)        # Creates frog, takes vehicles as parameters to then send these elements to the game loop 

if __name__ =="__main__":
    level = 1
    main(level)
