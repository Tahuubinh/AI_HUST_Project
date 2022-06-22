"""
This sliding-block puzzle solver implements the A-star algorithm to find the shortest list of moves
resulting in a solved state.
"""
__author__ = "Jasper Raynolds"
__license__ = "MIT"
__date__ = "February 2018"
import time

import heapq
import collections

#### BLOCK PUZZLE OBJECT ####

class Block_Puzzle:
	def __init__(self, blocks):
		"""
		Constructor. Takes a dictionary of integer-tuple pairs that describe block positions.
		Alternatively, takes a 2D list of integers that is then converted.
		"""
		if type(blocks) is list:
			self.blocks = self.__list_to_dict__(blocks)
		else :
			self.blocks = blocks

		self.width = self.__get_width__()
		self.height = int(len(self.blocks) / self.width)

	def __eq__(self, other):
		"""
		Equals function. Returns whether block dictionaries are equal.
		"""
		if other == None:
			return False
		return self.blocks == other.blocks

	def __lt__(self, other):
		"""
		Less-than function. Compares f-scores. If f-scores are equal, compares g-scores.
		"""
		if other == None:
			return False
		if fScore[self] == fScore[other]:
			return gScore[self] < gScore[other]
		return fScore[self] < fScore[other]

	def __hash__(self):
		"""
		Hash function. Hashes a frozenset of the blocks.
		"""
		return hash(frozenset(self.blocks.items()))

	def __list_to_dict__(self, blockList):
		"""
		Converts a 2D list of integers into a dictionary.
		"""
		dictionary = {}

		for row in range(len(blockList)):
			for col in range(len(blockList[0])):
				dictionary[blockList[row][col]] = (col, row);

		return dictionary

	def __get_width__(self):
		"""
		Returns the width of this puzzle.
		"""
		maxWidth = 0
		for value in self.blocks.values():
			maxWidth = max(value[0], maxWidth)

		return maxWidth + 1

	def to_string(self):
		"""
		Returns the state in an easy-to-read fashion.
		"""
		array = []

		for y in range(self.height):
			# print("y:",y)
			row = []
			for x in range(self.width):
				# print("x:",x)
				for block in self.blocks.items():
					# print(block)
					if block[1] == (x,y):
						row.append(block[0])
						break
			array.append(row)

		string = "\n".join("\t".join('%i' %x for x in y) for y in array)
		return string

	# def is_solvable(self):
	# 	"""
	# 	Returns true if the board is solvable, false if not.
	# 	This algorithmic solution provided by Adam Smith, Ph.D.
	# 	"""
	# 	# Flatten list, remove 0
	# 	flat = []
	# 	row0 = 0
	# 	for row in range(self.height):
	# 		for col in range(self.width):
	# 			for key in self.blocks:
	# 				if self.blocks[key][0] == col and self.blocks[key][1] == row:
	# 					if key == 0:
	# 						row0 = row
	# 					else:
	# 						flat.append(key)
			
	# 	# Count inversions
	# 	count = 0
	# 	for block in flat:
	# 		for tile2 in flat:
	# 			if flat.index(tile2) < flat.index(block) and tile2 > block:
	# 				count += 1

	# 	if self.height % 2 == 0:
	# 		if count % 2 == 0:
	# 			return True
	# 	elif (count + (self.height - row0 - 1)) % 2 == 0:
	# 		return True
	# 	return False

	def create_solved_puzzle(self):
		"""
		Returns a solved puzzle from this puzzle's dimensions.
		"""
		cellArr = []

		for row in range(self.height):
			boardRow = []
			for col in range(self.width):
				boardRow.append((row * self.width) + col + 1)
			cellArr.append(boardRow)

		cellArr[self.height - 1][self.width - 1] = 0

		puzzle = Block_Puzzle(cellArr)
		
		return puzzle

	def get_move(self, other):
		"""
		Interprets another puzzle as a move "U", "D", "L" or "R" from this one.
		"""
		# Compare both empty spaces
		thisEmpty = self.blocks[0]
		thatEmpty = other.blocks[0]
		move = (thisEmpty[0] - thatEmpty[0], thisEmpty[1] - thatEmpty[1])

		moveList = {(0,1): "D", (0,-1): "U", (1,0): "R", (-1,0): "L"}
		return moveList[move]

	def heuristic_estimate_manhattan(self, other):
		"""
		Finds the heuristic estimation of the cost to reach another state from this one.
		This heuristic is based on "manhattan distance."
		Returns the sum of each tile's orthogonal movement to reach its twin on the other board.
		"""
		estimate = 0

		for index in range(len(self.blocks)):
			estimate += abs(other.blocks[index][0] - self.blocks[index][0]) + abs(other.blocks[index][1] - self.blocks[index][1])

		return estimate

	def heuristic_estimate_misplaced_tiles(self, other):
		"""
		Finds the heuristic estimation of the cost to reach another state from this one.
		This heuristic is based on "misplaced tiles."
		Returns the number of tiles, not including the blank, that are in a different location from their twin on the other board.
		"""
		estimate = 0

		for index in range(1, len(self.blocks), 1):
			if self.blocks[index] != other.blocks[index]:
				estimate += 1

		return estimate

	def heuristic_estimate_maxSwap(self, other):
		"""
		Finds the heuristic estimation of the cost to reach another state from this one.
		This heuristic is based on "MaxSwap."
		Returns the number of moves it would take to convert this puzzle to the other if the empty tile could be freely switched.
		"""
		estimate = 0

		tempBlocks = dict(self.blocks)

		while(tempBlocks != other.blocks):
			for index in range(1, len(self.blocks), 1):
				if tempBlocks[index] == other.blocks[index]:
					continue
				if tempBlocks[0] == other.blocks[index]:
					tempBlocks[0] = tempBlocks[index]
					tempBlocks[index] = other.blocks[index]
					estimate += 1

		return estimate

	def get_neighbors(self, previous):
		"""
		Gets all adjacent neighbors of the state, minus the previous.
		This function gives 7 neighbors: 4 orthogonal, 4 diagonal, with the previous state trimmed.
		"""
		neighbors = []

		moves = ((-1,0),(1,0),(0,-1),(0,1))
		zeroLoc = self.blocks[0]

		for move in moves:
			newZeroLoc = (zeroLoc[0] + move[0], zeroLoc[1] + move[1])
			# skip this state if we've moved off the board
			if newZeroLoc[0] < 0 or newZeroLoc[1] < 0 or newZeroLoc[0] > self.width-1 or newZeroLoc[1] > self.height-1:
				# print("we've moved off the board.")
				continue
			# skip this state if it's the same as the previous
			if previous and previous.blocks[0] == newZeroLoc:
				# print("this is just the same!")
				continue


			newBlocks = dict(self.blocks)
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

#### A-STAR ALGORITHM ####

def aStar(start, goal):
	"""
	A star search algorithm. Takes a start state and an end state.
	While there are available moves, loops through them and exits if the end is found.
	Returns the list of states that are the "quickest" way to the end.
	"""
	# The set of states already evaluated
	closedSet = set()

	# For each node, which node it can most efficiently be reached from.
	# If a node can be reached from many start, cameFrom will eventually contain the
	# most efficient previous step.
	cameFrom = {}

	# For each node, the total cost of getting from the start node to the goal
	# by passing by that node. That value is partly known, partly heuristic.
	# This variable is global for the Block_Puzzle object's __lt__ method.
	global fScore
	fScore = collections.defaultdict(lambda: float("inf"))

	# For each node, the cost of getting from the start node to that node.
	# This variable is global for the Block_Puzzle object's __lt__ method.
	global gScore
	gScore = collections.defaultdict(lambda: float("inf"))

	# The cost of going from start to start is zero.
	gScore[start] = 0

	# The heap of currently discovered state that are not evaluated yet.
	# Initially, only the start state is known.
	openHeap = [start]
	heapq.heapify(openHeap)

	# For the first node, that value is completely heuristic.
	fScore[start] = start.heuristic_estimate_manhattan(goal)

	# The set of neighbors with equal f-scores to their progenitor.
	# This set is emptied first to avoid needless push/pop from the heap.
	equalSet = set()

	# While there are yet nodes to inspect,
	while openHeap:
		# Get the lowest f-score state not yet evaluated.
		current = heapq.heappop(openHeap)

		print(len(openHeap))

		# Skip this state if it's a duplicate of one that's already been evaluated.
		if current in closedSet:
			continue

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

		# make sure we don't visit this state again.
		closedSet.add(current)

		# For each possible neighbor of our current state,
		for neighbor in current.get_neighbors(cameFrom.get(current)):
			# Skip it if it's already been evaluated
			if neighbor in closedSet:
				continue

			tentative_gScore = gScore[current] + 1
			# If this path costs less than previous paths here...
			if tentative_gScore < gScore[neighbor]:
				# Update the values for this state.
				cameFrom[neighbor] = current
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = gScore[neighbor] + (1.0001 * neighbor.heuristic_estimate_manhattan(goal))
			
			# Finally, add it to our open heap
			heapq.heappush(openHeap, neighbor)

	return None

#### SOLVER FUNCTION ####

def solve(cellArr):
	"""
	Solver function. Takes a 2D list of integers, starting from and including 0, in equal-length rows,
	and returns a list of single-letter string moves (e.g. "U", "R", "D")
	"""
	# Error handling
	if type(cellArr) is not list or type(cellArr[0]) is not list:
		print("please pass a 2D integer list to this function.")
		return None
	rowLength = len(cellArr[0])
	for row in cellArr:
		if len(row) != rowLength:
			print("all rows in the 2D integer list must be of equal length.")
			return None

	# from the cell list provided, create a Block Puzzle.
	puzzle = Block_Puzzle(cellArr)

	# is this puzzle solvable?
	# if not puzzle.is_solvable():
	# 	return None

	# find the solution puzzle for the given puzzle.
	goal = puzzle.create_solved_puzzle()

	# run A* search algorithm.
	path = aStar(puzzle, goal)

	# convert into single-letter moves.
	moves = []
	for index in range(len(path)-1):
		moves.append(path[index].get_move(path[index+1]))
	return moves

#### TESTING ####

# hard = [[6,5,2,3],
# 		[0,7,11,4],
# 		[9,1,10,8],
# 		[15,14,13,12]]
# print(solve(hard))

# medium = [[1,2,3,4],
# 		  [0,7,11,5],
# 		  [9,6,10,8],
# 		  [15,14,13,12]]
# print(solve(medium))

# easy = [[1,2,3,4],
# 		[0,5,6,7],
# 		[9,10,11,8]]
# print(solve(easy))

board = [[8,5,1],
		[6,7,0],
		[3,2,4]]
begin = time.time()
print(solve(board))
print(time.time() - begin)