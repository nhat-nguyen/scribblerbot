from myro import *
from bfs import bfs
init("/dev/tty.IPRE6-197621-DevB")

def rightNinety():
	# turnRight(0.5, 1.15)
	# turnRight(0.3, 2.1)
	turnRight(0.25, 3.05)


def leftNinety():
	# turnLeft(0.3, 2.1)
	turnLeft(0.25, 3.05)


def getLines():
	return sum(get('line'))

def moveForward():
	# while (getLines() >= 1):
	# 	forward(0.1)
	# else:
	# 	stop()
	forward(0.6, 1.05)

def knightBlocks(f, n):
	while(n != 0):
		f()
		n -= 1
		# if (n != 0): forward(0.1, 1)
		# if (d): backward(0.1,1.28)


def knightMoves(i, j):
	if (i > 0):
		knightBlocks(moveForward, abs(i))
	if (i < 0):
		rightNinety()
		rightNinety()
		knightBlocks(moveForward, abs(i))
	if (j < 0):
		if (i < 0):
			leftNinety()
		else:
			rightNinety()
		knightBlocks(moveForward, abs(j))
		leftNinety()
	if (j > 0):
		if (i > 0):
			leftNinety()
		else:
			rightNinety()
		knightBlocks(moveForward, abs(j))
		rightNinety()
	beep(1, 440)
# knightMoves(1,2)
# rightNinety()

# start = (0,0)
# while (True):
# 	end = (input(),input())
# 	steps = bfs(start,end)
# 	for cur in steps[1:]:
# 		delta = (cur[0]-start[0],cur[1]-start[1])
# 		knightMoves(delta)
# 		start = cur
