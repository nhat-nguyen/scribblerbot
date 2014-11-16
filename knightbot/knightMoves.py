from myro import *
init("/dev/tty.IPRE6-197621-DevB")

def rightNinety():
	turnRight(0.5, 1.15)

def leftNinety():
	turnLeft(0.5, 1.15)

def getLines():
	return sum(get('line'))

def moveForward():
	while (getLines() >= 1):
		forward(0.1)
	else:
		stop()

def moveBackward():
	rightNinety()
	rightNinety()
	moveForward()

def knightBlocks(f, n):
	while(n != 0):
		f()
		n -= 1
		forward(0.1, 1)

def knightMoves(i, j):
	if (i > 0):
		knightBlocks(moveForward, abs(i))
	if (i < 0):
		knightBlocks(moveBackward, abs(i))
	if (j > 0):
		if (i < 0):
			leftNinety()
		else:
			rightNinety()
		knightBlocks(moveForward, abs(j))
		leftNinety()
	if (j < 0):
		if (i > 0):
			leftNinety()
		else:
			rightNinety()
		knightBlocks(moveForward, abs(j))
		rightNinety()
