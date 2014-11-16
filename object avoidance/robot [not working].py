from myro import *
init("/dev/tty.IPRE6-197621-DevB")

def is_clear(rang=1000, orient="center"):
    s = 0
    sampl = 5#don't make too high!
    for i in range(sampl):
        s += getObstacle(orient)
    s /= sampl
    if s < rang:
        return True
    else:
        return False

def go(v=0.2):
    while(is_clear()):#right for 45
        forward(v)
    stop()
    forward(0.1, 1.2)#calibrate!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def turn_clear_R(v=0.2):
    while(not is_clear()):
        turnRight(v)
    stop()

def turn_clear_L(v=0.2):
    while(not is_clear()):
        turnLeft(v)
    stop()

def turn_block_R(v=0.2):
    while(is_clear()):
        turnRight(v)
    stop()

def turn_block_L(v=0.2):
    while(is_clear()):
        turnLeft(v)
    stop()

def turn_corner(v=0.3):
    while(is_clear(700, "right")):
        motors(v, 0.1)
    stop()

def turn_R():
    turnRight(0.2, 1.4)
    stop()

def turn_L():
    turnLeft(0.2, 1.4)
    stop()

def path_90():
    #setName("shit")
    count = 0
    go()
    turn_clear_L()
    turn_R()
    while(not is_clear(1000, "right")):
        turn_L()
        forward(0.5, 0.5)
        turn_clear_L()
        turn_R()
        backward(0.1, 0.2)
        count += 1
    backward(0.1, 0.2)
    turn_L()
    turn_L()
    turn_corner()
    while(not is_clear(1000, "right")):
        turn_L()
        forward(0.5, 0.5)
        turn_clear_L()
        turn_R()
        backward(0.1, 0.2)
    backward(0.1, 0.2)
    turn_L()
    turn_L()
    turn_corner()
    turn_block_R()
    turn_clear_L()
    for i in range(count - 2):
        forward(0.5, 0.5)
    turn_clear_L()
    turnLeft(0.3, 2.4)
    forward(1, 2)
    beep(2, 440)

def path_45():
    print("i'm not done yet")

path_90()