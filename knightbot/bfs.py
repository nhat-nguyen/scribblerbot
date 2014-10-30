import numpy
from random import *

graph = numpy.zeros((8, 8))

start = (randint(0, 7), randint(0, 7))
stop = (randint(0, 7), randint(0, 7))

print "Start: ", start
print "Stop: ", stop

print "------------------------------\n"

frontier = [start]
came_from = {}

stopFind = False
while len(frontier) > 0:
	# directions that the knight can move
	movement = [((frontier[0])[0] - 1, (frontier[0])[1] - 2), ((frontier[0])[0] + 1, (frontier[0])[1] - 2), ((frontier[0])[0] - 1, (frontier[0])[1] + 2), ((frontier[0])[0] + 1, (frontier[0])[1] + 2), ((frontier[0])[0] - 2, (frontier[0])[1] - 1), ((frontier[0])[0] - 2, (frontier[0])[1] + 1), ((frontier[0])[0] + 2, (frontier[0])[1] - 1), ((frontier[0])[0] + 2, (frontier[0])[1] + 1)]

	for i in movement:
		# check only the valid movement
		if i[0] >= 0 and i[0] < 8 and i[1] >= 0 and i[1] < 8:

			if not graph[i[0]][i[1]]:
				graph[i[0]][i[1]] = i[0] + i[1] / 10.0
				if (i[0], i[1]) == stop:
					graph[i[0]][i[1]] = "99"
					stopFind = True
				frontier.append(i)
				if i not in came_from:
					came_from[i] = frontier[0]
				if stopFind:
					break
	if stopFind:
		break

	del frontier[0]

print graph

current = stop
steps = [current]
while current != start:
	current = came_from[current]
	steps.append(current)


print "\n------------------------------\n"


i = len(steps) - 1

while i >= 0:
	print steps[i]
	i -= 1
