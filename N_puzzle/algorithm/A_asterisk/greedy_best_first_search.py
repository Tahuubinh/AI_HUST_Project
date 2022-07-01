import time
import heapq
import collections

from sklearn import neighbors

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

    def create_solved_puzzle(self):
        """
        Returns a solved puzzle from this puzzle's dimensions.
        """
        cellArr = []

        for row in range(self.width):
            boardRow = []
            for col in range(self.width):
                boardRow.append((row * self.width) + col + 1)
            cellArr.append(boardRow)

        cellArr[self.width - 1][self.width - 1] = 0

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
        zeroLoc = self.blocks[0]         # {value: (x, y)}

        for move in moves:
            newZeroLoc = (zeroLoc[0] + move[0], zeroLoc[1] + move[1])
            # skip this state if we've moved off the board
            if newZeroLoc[0] < 0 or newZeroLoc[1] < 0 or newZeroLoc[0] > self.width-1 or newZeroLoc[1] > self.width-1:
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

class BestFirstSearch:
    def __init__(self, board, width) -> None:
        self.board = board
        self.width = width

    def run_BestFirstSearch(self, start, goal):
       
        closedSet = set()

        cameFrom = {}

        global fScore
        fScore = collections.defaultdict(lambda: float("inf"))

        openHeap = [start]
        heapq.heapify(openHeap)

        fScore[start] = start.heuristic_estimate_manhattan(goal)

        while openHeap:
            current = heapq.heappop(openHeap)

            if current in closedSet:
                continue

            if current == goal:
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                path.reverse()
                return cnt

            closedSet.add(current)

            for neighbor in current.get_neighbors(cameFrom.get(current)):
                if neighbor in closedSet:
                    continue

                cameFrom[neighbor] = current
                fScore[neighbor] = neighbor.heuristic_estimate_manhattan(goal)
                
                heapq.heappush(openHeap, neighbor)

    #### SOLVER FUNCTION ####

    def findMinimumSteps(self):
        start = Block_Puzzle(self.board)

        goal = start.create_solved_puzzle()

        begin = time.time()
        num_steps = self.run_BestFirstSearch(start, goal)
        end = time.time()

        return end - begin, num_steps


#### TESTING ####

# board = [[6,5,2,3],
#         [0,7,11,4],
#         [9,1,10,8],
#         [15,14,13,12]]
# print(solve(hard))

# medium = [[1,2,3,4],
#           [0,7,11,5],
#           [9,6,10,8],
#           [15,14,13,12]]
# print(solve(medium))

# easy = [[1,2,3,4],
#         [0,5,6,7],
#         [9,10,11,8]]
# print(solve(easy))

# board = [[8,5,1],
#         [6,7,0],
#         [3,2,4]]

# board = [[0,2,4,8],
#         [3,1,6,12],
#         [5,9,10,7],
#         [13,14,11,15]]

# a = BestFirstSearch(board, 4)
# duration, num_steps = a.findMinimumSteps()
# print(duration, num_steps)