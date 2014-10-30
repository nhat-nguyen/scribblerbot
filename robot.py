def is_clear(rang=1000, orient="center", sampl=3):
    s = 0
    for i in range(sampl):
        n += getObstacle(orient)
    s /= x
    if s < rang:
        return True
    else:
        return False

def go(v=0.5):
    while(is_clear(1100)):
        forward(v)
    stop()
    forward(0.1, 1)

def turn_clear(direct="R", v=0.2):
    if(direct="R"):
        while(not is_clear()):#enter range, orientation, sample
            turnRight(v)
    elif(direct="L"):
        while(not is_clear()):
            turnLeft(v)
    stop()

def turn_block(direct="R", v=0.2):
    if(direct="R"):
        while(is_clear()):#enter range, orientation, sample
            turnRight(v)
    elif(direct="L"):
        while(is_clear()):
            turnLeft(v)
    stop()

def turn_corner():
    while(is_clear()):#enter range, orientation, sample
        motors(0.3, 0)
    stop()
