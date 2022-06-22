import math
import heapq
import collections
import copy

# For each node, the total cost of getting from the start node to the goal
# by passing by that node. That value is partly known, partly heuristic.
fScore = collections.defaultdict(lambda: float("inf"))

class Block_Puzzle:
    def __init__(self, blocks):

        if type(blocks) is list:
            self.blocks = self.__list_to_dict__(blocks)
            print(self.blocks)
        else:
            self.blocks = blocks

        self.width = self.__get_width__()
        self.height = int(len(self.blocks) / self.width)

    def __eq__(self, other):

        if other == None:
            return False
        return self.blocks == other.blocks

    def __lt__(self, other):
        if other == None:
            return False
        return fScore[self] < fScore[other]

    def __hash__(self):
        return hash(frozenset(self.blocks.items()))

    def __list_to_dict__(self, blockList):
        dictionary = {}

        for row in range(len(blockList)):
            for col in range(len(blockList[0])):
                dictionary[blockList[row][col]] = (col, row);

        return dictionary

    def __get_width__(self):
        maxWidth = 0
        for value in self.blocks.values():
            maxWidth = max(value[0], maxWidth)

        return maxWidth + 1

    def to_string(self):
        array = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                for block in self.blocks.items():
                    if block[1] == (x,y):
                        row.append(block[0])
                        break
            array.append(row)

        string = "\n".join("\t".join('%i' %x for x in y) for y in array)
        return string

    def heuristic_estimate_manhattan(self, other):
        estimate = 0

        for index in range(len(self.blocks)):
            estimate += abs(other.blocks[index][0] - self.blocks[index][0]) + abs(other.blocks[index][1] - self.blocks[index][1])

        return estimate

    def get_neighbors(self, previous):
        neighbors = []

        moves = ((-1,0),(1,0),(0,-1),(0,1))
        zeroLoc = self.blocks[0]

        for move in moves:
            # swap 0 and whatever
            newBlocks = copy.deepcopy(self.blocks)
            newZeroLoc = (zeroLoc[0] + move[0], zeroLoc[1] + move[1])
            # skip this state if we've moved off the board
            if newZeroLoc[0] < 0 or newZeroLoc[1] < 0 or newZeroLoc[0] > self.width-1 or newZeroLoc[1] > self.height-1:
            	# print("we've moved off the board.")
                continue
            # skip this state if it's the same as the previous
            if previous and previous.blocks[0] == newZeroLoc:
            	# print("this is just the same!")
                continue

            # move the 0
            newBlocks[0] = newZeroLoc

            # move whatever's in that location...
            # to the previous one
            for face, location in newBlocks.items():
                if face != 0 and location == newZeroLoc:
                    newBlocks[face] = zeroLoc

            neighbor = Block_Puzzle(newBlocks)
            neighbors.append(neighbor)

        return neighbors
		
def aStar(start, goal):
	"""
	A star search algorithm. Takes a start state and an end state.
	While there are available moves, loops through them and exits if the end is found.
	Returns the list of states that are the "quickest" way to the end.
	"""
	# The dictionary of states already evaluated
	closedDict = {}

	# For each node, which node it can most efficiently be reached from.
	# If a node can be reached from many start, cameFrom will eventually contain the
	# most efficient previous step.
	cameFrom = {}

	# For each node, the cost of getting from the start node to that node.
	gScore = collections.defaultdict(lambda: float("inf"))

	# The cost of going from start to start is zero.
	gScore[start] = 0

	# The heap of currently discovered state that are not evaluated yet.
	# Initially, only the start state is known.
	openHeap = [start]
	heapq.heapify(openHeap)

	# For the first node, that value is completely heuristic.
	fScore[start] = start.heuristic_estimate_manhattan(goal)

	# While there are yet nodes to inspect,
	while(len(openHeap) > 0):
		# Pop the lowest f-score state off. 
		current = heapq.heappop(openHeap)

		# print(len(openHeap))

		# If we've reached the goal:
		if current == goal:
			# return the list of states it took to get there.
			path = []
			path.append(current)
			step = current
			while(cameFrom.get(step)):
				path.append(cameFrom[step])
				step = cameFrom[step]
			path.reverse()
			return path

		# make sure we won't visit this state again.
		closedDict[current] = True

		# For each possible neighbor of our current state,
		for neighbor in current.get_neighbors(cameFrom.get(current)):
			# Skip it if it's already been evaluated
			if neighbor in closedDict:
				continue

			# Add it to our open heap
			heapq.heappush(openHeap, neighbor)

			tentative_gScore = gScore[current] + 1
			# If it takes more to get here than another path to this state, skip it.
			if tentative_gScore >= gScore[neighbor]:
				continue

			# If we got to this point, add it!
			cameFrom[neighbor] = current
			gScore[neighbor] = tentative_gScore
			fScore[neighbor] = gScore[neighbor] + neighbor.heuristic_estimate_manhattan(goal)

	return None

start = Block_Puzzle([[1,3,4,2],[0,5,6,7],[9,10,11,8]])
goal = Block_Puzzle([[1,2,3,4],[5,6,7,8],[9,10,11,0]])

#start = Block_Puzzle([[0,3,1],[4,2,6],[7,5,8]])
#start = Block_Puzzle([[0,1,3],[4,2,6],[7,5,8]])
start = Block_Puzzle([[1,0,3],[4,2,6],[7,5,8]])
goal = Block_Puzzle([[1,2,3],[4,5,6],[7,8,0]])
path = aStar(start, goal)
for state in path:
	print(state.to_string())
	print()