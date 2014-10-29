import numpy

graph = numpy.zeros((8, 8))

x = 0
y = 0


dst = (1, 1)
# def knightMove(pos, dst, graph, frontier):

# 	movement = [((frontier[0])[0] - 1, (frontier[0])[1] - 2), ((frontier[0])[0] + 1, (frontier[0])[1] - 2), ((frontier[0])[0] - 1, (frontier[0])[1] + 2), ((frontier[0])[0] + 1, (frontier[0])[1] + 2), ((frontier[0])[0] - 2, (frontier[0])[1] - 1), ((frontier[0])[0] - 2, (frontier[0])[1] + 1), ((frontier[0])[0] + 2, (frontier[0])[1] - 1), ((frontier[0])[0] + 2, (frontier[0])[1] + 1)]

# 	del frontier[0]

# 	for i in movement:
# 		if not graph[i[0]][i[1]]:
# 			graph[i[0]][i[1]] = 1
# 			if (i[0], i[1]) == dst:
# 				break
# 			frontier.append((i[0], i[1]))


frontier = [(x, y)]

stop = False

while len(frontier) > 0:
	# knightMove(frontier[0], (1, 1), graph, frontier)
	movement = [((frontier[0])[0] - 1, (frontier[0])[1] - 2), ((frontier[0])[0] + 1, (frontier[0])[1] - 2), ((frontier[0])[0] - 1, (frontier[0])[1] + 2), ((frontier[0])[0] + 1, (frontier[0])[1] + 2), ((frontier[0])[0] - 2, (frontier[0])[1] - 1), ((frontier[0])[0] - 2, (frontier[0])[1] + 1), ((frontier[0])[0] + 2, (frontier[0])[1] - 1), ((frontier[0])[0] + 2, (frontier[0])[1] + 1)]
	print '----------'

	del frontier[0]

	print movement
	for i in movement:
		print graph
		print '------'
		if ([i])[0] > 0 and ([i])[0] < 8 and ([i])[1] > 0 and ([i])[1] < 8:
			if not graph[i[0]][i[1]]:
				graph[i[0]][i[1]] = 1
				if (i[0], i[1]) == dst:
					graph[i[0]][i[1]] = 9
					stop = True
					break
				frontier.append((i[0], i[1]))
	if stop:
		break




print graph