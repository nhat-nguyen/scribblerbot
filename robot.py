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

def go(v=0.2):#ok
    while(is_clear(1000)):
        forward(v)
    stop()
    #forward(0.1, 0.5)

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
    while(is_clear(600, "right")):#enter range, orientation, sample
        motors(v, 0.1)
    stop()

def turn_R():
    turnRight(0.2, 1.2)
    stop()

def turn_L():
    turnLeft(0.2, 1.2)
    stop()

setName("retarded")
count = 0
go()
turn_clear_L()
turn_R()
while(not is_clear()):
    turn_L()
    forward(0.5, 0.5)
    turn_clear_L()
    turn_R()
    count += 1
backward(0.1, 0.2)
turn_L()
turn_L()
turn_corner()
while(not is_clear()):
    turn_L()
    forward(0.5, 0.5)
    turn_clear_L()
    turn_R()
backward(0.1, 0.2)
turn_L()
turn_L()
turn_corner()
turn_clear_L()
for i in range(count):
    forward(0.5, 0.5)
turn_clear_L
turnLeft(0.3, 2.4)
beep(2, 440)