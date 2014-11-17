from myro import *
from bfs import bfs
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

def knightBlocks(f, n):
	while(n != 0):
		f()
		n -= 1
		forward(0.1, 1)

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

knightBlocks(moveForward,1)

#rightNinety()

# start = (0,0)
# while (True):
# 	end = (input(),input())
# 	steps = bfs(start,end)
# 	for cur in steps[1:]:
# 		delta = (cur[0]-start[0],cur[1]-start[1])
# 		knightMoves(delta)
# 		start = cur
