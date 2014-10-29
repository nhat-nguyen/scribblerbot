from myro import *
init("/dev/tty.IPRE6-197621-DevB")
import time#or use currentTime()
t1 = 0
t2 = 0
v = 0.5
count = 0
time_list = []
flag = False

def get_time(t1, t2):
    dt = t2 - t1
    return dt

def is_clear():
    n = 0
    #for i in range(5):
    for j in range(3):
        n += getObstacle()[j]
    if n < 900:
        return True
    else:
        return False

while(is_clear()):
    forward(1, 0.1)

t1 = time.time()
while(not is_clear()):
    turnRight(v, 0.1)
t2 = time.time()
time_list.append(get_time(t1, t2))
#records time for first turn @ v = 0.5: to turn 45/90 deg.

while(not flag):
    forward(v, 0.1)
    count += 0.1
    turnLeft(v, time_list[0])
    if(not is_clear()):
        turnRight(v, time_list[0])
    elif(is_clear()):
        flag = True


