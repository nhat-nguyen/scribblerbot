from myro import *
init("/dev/tty.IPRE6-197621-DevB")

def turn_45R():
    turnRight(0.3, 1.2)
def turn_90R():
    turnRight(0.3, 2.4)
def turn_45L():
    turnLeft(0.3, 1.2)
def turn_90L():
    turnLeft(0.3, 2.4)

def is_clear():
    n = 0
    #for i in range(5):
    for j in range(3):
        n += getObstacle()[j]
    if n < 900:
        return True
    else:
        return False
"""
def check_clear(): #assume you're in a clear path first.
    move_x()
    turn_90L()
    if not is_clear():
        turn_90R()
        return False
    elif is_clear():
        return True #the way is clear now.
"""    
def move_x():
    forward(0.1, 1)
    #forward(.5, 1)

def get_x_count():
    return count

def path_45():
    #stop
    count = 0
    turn_45L()
    while not is_clear():
        turn_90R()
        move_x()
        turn_90L()
        count += 1

    #buffer
    move_x()
    
    for x in range(count):
        move_x()
    turn_45R()
    forward(1, 5)

getBattery()
for i in range(4):
    turnRight(.3, 1.2)
