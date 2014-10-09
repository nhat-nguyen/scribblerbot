from myro import *

init("/dev/tty.IPRE6-197621-DevB")

#print(getBattery())
#beep(2, 523)
#beep(0.5, 670)

#1 if clear; 0 if blocked. 0/l:L/R
# getObstacle(center/left/right)

def no_obstacle(block):
	#status = True
	l = getObstacle("left") 
	c = getObstacle("center")
	r = getObstacle("right")
	print(l, c, r)
	if l + c + r >= 700:
	    return False
	else:
		return True		
	return status
	
#checks left side for obstruction

def avoid():
    blocked = True
    while(blocked):
		turnLeft(0.2, 3)
		a = getObstacle()
		a = a[0] + a[1] + a[2]
		if a == 0:
			turnLeft(0.2, 1)
		if no_obstacle():
			blocked = False
		else:
			turnRight(0.2, 3)
			forward(0.3, 2)

"""
def avoid():
	turnLeft(0.2, 3)
	if no_obstacle():
		turnRight(0.2, 3)
	else:
	"""	

while(no_obstacle() or timeRemaining(123)):
    if not no_obstacle():
		turnRight(0.2, 3)
		forward(0.3, 1)
		avoid()
	forward(0.3)