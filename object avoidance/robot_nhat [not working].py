from myro import *

init("/dev/tty.IPRE6-197621-DevB")

def average(a):
	for i in range(0, 3):
		a[i] = 0
	for i in range (0, 2):
		a[0] += getObstacle("left") 
		a[1] += getObstacle("center") 
		a[2] += getObstacle("right")
	for i in range(0, 3):
		a[i] /= 2
	print a

def obstaclesUpFront():
	a = [0, 0, 0]
	average(a)
	if (a[0] + a[1] + a[2]) / 3.0 >= 900:
		return True

	return False

def obstacleRotate():
	a = [0, 0, 0]
	average(a)
	if getObstacle("right") > 90:
		return True
	return False

def rotate45():
	turnLeft(0.3, 1.2)
	if obstacleRotate():
		turnLeft(0.3, 1.2)
		return 2

	return 1

def rotate90CW():
	# turnRight(0.3, 2.4)
	turnRight(0.6, 1)

def rotate90CCW():
	# turnLeft(0.3, 2.4)
	turnLeft(0.6, 1)

def moveForward(steps):
	forward(0.1, 1)
	steps += 1
	return steps

distance = 1

while (timeRemaining(10)):
	while not obstaclesUpFront():
		forward(0.5, 1)
		
	if obstaclesUpFront():
		rotate90CCW()
		beingBlocked = True

		while beingBlocked:
			distance = moveForward(distance)
			rotate90CW()
			if obstaclesUpFront() or obstacleRotate():
				rotate90CCW()
			else:
				beingBlocked = False

		rotate90CCW()
		for i in range(0, 4):
			distance = moveForward(distance)

		# begin to move along the sides of the box

		rotate90CW() # rotate to the other sides
		forward(1, 1) # move fast to get pass the edges of the sides


		rotate90CW() # check for obstacle to the right

		while obstaclesUpFront():
			rotate90CCW()
			forward(0.5, 1)
			rotate90CW()

		rotate90CCW()
		forward(0.5, 1) # to avoid the edges
		rotate90CW()

		for i in range(0, distance):
			forward(0.1, 1)

		rotate90CCW()

	forward(0.1)


stop()