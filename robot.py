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

def turn_clear_R(v=0.2):
    while(not is_clear()):#enter range, orientation, sample
        turnRight(v)
    stop()

def turn_block(v=0.2):
    while(is_clear()):#enter range, orientation, sample
        turnRight(v)
    stop()

def turn_corner(v=0.3):
    while(is_clear()):#enter range, orientation, sample
        motors(v, 0)
    stop()
