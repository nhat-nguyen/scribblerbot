from random import *
from collections import deque
def bfs (start, stop):
    graph = [[0]*6 for _ in range (6)]

    #start = (randint(0, 7), randint(0, 7))
    #stop = (randint(0, 7), randint(0, 7))

    # print "Start: ", start
    # print "Stop: ", stop

    frontier = deque([start])	#can efficiently pop from both ends of the list
    came_from = {}

    stopFind = False
    graph[start[0]][start[1]] = 1

    while len(frontier) > 0:
        movement = [] # directions that the knight can move

        # dequeue operation (not to be confused with deque data structure in python)
        pos = frontier.popleft()

        #checks all knight's moves from first item in queue
        for i in range (-2,3):
                for j in range(-2,3):
                        if abs(i)+abs(j)==3:
                                movement.append((pos[0]+i,pos[1]+j))

        for i in movement:
            # check only the valid movement
            if 0 <= i[0] < 6 and 0 <= i[1] < 6:
                if not graph[i[0]][i[1]]:
                    graph[i[0]][i[1]] = graph[pos[0]][pos[1]]+1
                    if i == stop:
                        stopFind = True
                        
                    frontier.append(i) #enqueue operation

                    # could not have come from i if has not been visited yet;
                    # already checked with if statement
                    came_from[i] = pos
                    if stopFind:
                        break
        if stopFind:
            break

    #complete graph with all possible moves and move numbers from start stop
    # currently not needed !
    # for i in range(6):
    #         print ' '.join(map(str,graph[i]))

    current = stop

    # please note that the steps in this list are in reverse order
    steps = [current]

    while current != start:
        current = came_from[current]
        steps.append(current)

    # print "------------------------------"

    #list of moves from start to stop
    # for i in reversed (range(len(steps))):
    #     print steps[i]

    # print "------------------------------"

    #shows moves and move numbers to go from start to stop
    # for i in range (6):
    #     print ' '.join(map(lambda x: str(graph[i][x] * int((i,x) in steps)),range(8)))

    # print "------------------------------"
    return steps[::-1]

# a = bfs((randint(0, 7), randint(0, 7)), (randint(0, 7), randint(0, 7)))

# print a
