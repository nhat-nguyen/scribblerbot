from myro import *
init("/dev/tty.IPRE6-197621-DevB")

def is_clear(r=900, orient="center"):
    n = 0
    x = 10
    for i in range(x):
        n += getObstacle(orient)
    n /= x
    if n < r:
        return True
    else:
        return False
def go():
    while(is_clear(1100)):
        forward(0.5)
    stop()
    
def turn_45R():
    turnRight(0.3, 1.2)
def turn_90R():
    turnRight(0.3, 2.4)
def turn_45L():
    turnLeft(0.3, 1.2)
def turn_90L():
    turnLeft(0.3, 2.4)

def turn_block_R():#turn until blocked
    while(is_clear()):
        turnRight(0.2)
    stop()
        
def turn_block_L():
    while(is_clear()):
        turnLeft(0.2)
    stop()
        
def turn_clear_R():#turn till clear
    while(not is_clear()):
        turnRight(0.2)
    stop()
        
def turn_clear_L():
    while(not is_clear()):
        turnLeft(0.2)
    stop()

def side(count = 0):
    if(count == 0):
        n = 0
        while(not is_clear(500, "right")):
            backward(0.1, 0.1)
            turn_clear_L()
            forward(0.5, 0.5)
            turn_90R()
            n += 1
        return n
    elif(count < 0):
        for i in range(count):
            forward(0.5, 0.5)
        return 0
    #or turn_block_R, then turn_90L()?

def corner():
    turn_90L()
    forward(0.1, 1)
    turn_block_R()
    turn_clear_L()
    beep(1, 440)

def path_90():
    count = 0
    go()
    forward(0.1, 1)
    count = side()
    corner()
    side()
    corner()
    side(count)
    turn_90L()
    forward(1, 1)
    beep(1, 220)

def path_45():
    count = 0
    go()
    forward(0.1, 1)
    count = side()
    corner()
    side(count)
    turn_45L()
    forward(1, 1)
    beep(1, 220)
    
path_90()
