from myro import *
init("/dev/tty.IPRE6-197621-DevB")

#left side of box!

def findClear():
    count = 0
    while getObstacle("right") > 10:
        turnLeft(0.1, 0.1)
        count += 1
    return count


def is_clear(rang=1100, orient="center"):
    s = 0
    sampl = 5#don't make too high!
    for i in range(sampl):
        s += getObstacle(orient)
    s /= sampl
    if s < rang:
        return True
    else:
        return False

def go(v=0.2):#ok
    while(is_clear(1050)):
        forward(v)
    stop()
    forward(0.1, 0.3)

def turn_clear_R(v=0.2):
    while(not is_clear()):#enter range, orientation, sample
        turnRight(v)
    stop()

def turn_clear_L(v=0.2):
    while(not is_clear()):#enter range, orientation, sample
        turnLeft(v)
    stop()

def turn_block_R(v=0.2):
    while(is_clear()):#enter range, orientation, sample
        turnRight(v)
    stop()

def turn_block_L(v=0.2):
    while(is_clear()):#enter range, orientation, sample
        turnLeft(v)
    stop()

def turn_corner(v=0.3):
    while(is_clear(500, "right")):#enter range, orientation, sample
        motors(v, 0.1)
    stop()

def turn_R():
    turnRight(0.2, 1.4)
    stop()

def turn_L():
    turnLeft(0.2, 1.4)
    stop()

def path45():
    setName("shit")
    count = 0
    go()
    countAngle = findClear()
    turn_R()
    while(not is_clear(700, "right")):
        turn_L()
        forward(0.5, 0.5)
        turn_clear_L()
        turn_R()
        backward(0.1, 0.2)
        count += 1
    backward(0.1, 0.4)
    turn_L()
    turn_L()
    turn_corner()

    backward(0.1, 0.2)
    while getObstacle("right") > 10:
        turnLeft(0.1, 0.1)

    turnLeft(0.1, 1)

    for i in range(count - 5):
        forward(0.5, 0.5)
    """
    for i in range(0, countAngle):
        turnLeft(0.1, 0.1)
    """
    turnLeft(0.3, 1.2)
    forward(1, 2)
    beep(2, 440)

path45()