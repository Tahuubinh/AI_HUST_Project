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
                dictionary[blockList[row][col]] = (col, row)
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
        #print("Estimate: " + str(estimate))
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

    def heuristic_estimate_linear_conflict(self, other):
        """
        https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
        """
        estimate = 0

        for index in range(len(self.blocks)):
            x_cur = self.blocks[index][0]
            y_cur = self.blocks[index][1]
            x_goal = other.blocks[index][0]
            y_goal = other.blocks[index][1]
            if x_cur == x_goal and y_cur == y_goal:
                continue

            estimate += abs(x_goal - x_cur) + abs(y_goal - y_cur)

            if x_cur == x_goal:
                index_begin = x_cur * self.width
                index_end = index_begin + y_goal - 1
                for i in range(index_begin, index_end):
                    if self.blocks[i][0] == x_cur and self.blocks[i][1] > y_cur:
                        estimate += 2

            elif y_cur == y_goal:
                index_begin = y_cur
                index_end = (x_goal - 1) * self.width + y_cur
                for i in range(index_begin, index_end, self.width):
                    if self.blocks[i][1] == y_cur and self.blocks[i][0] > x_cur:
                        estimate += 2

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

class AASTERISK:
    def __init__(self, board, width) -> None:
        self.board = board
        self.width = width

    def run_Astar(self, start, goal):
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
        # print(goal.blocks)

        # While there are yet nodes to inspect,
        while openHeap:
            # Get the lowest f-score state not yet evaluated.
            current = heapq.heappop(openHeap)

            # print(len(openHeap))

            # Skip this state if it's a duplicate of one that's already been evaluated.
            if current in closedSet:
                continue

            # If we've reached the goal:
            if current == goal:
                # return the list of states it took to get there.
                end = time.time()
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                ##path.reverse()
                return cnt, end, path

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
                    fScore[neighbor] = gScore[neighbor] + neighbor.heuristic_estimate_manhattan(goal)
                
                # Finally, add it to our open heap
                heapq.heappush(openHeap, neighbor)

    #### SOLVER FUNCTION ####

    def findMinimumSteps(self):
        # from the cell list provided, create a Block Puzzle.
        start = Block_Puzzle(self.board)

        # find the solution puzzle for the given puzzle.
        goal = start.create_solved_puzzle()

        # run A* search algorithm.
        begin = time.time()
        num_steps, end, path = self.run_Astar(start, goal)

        # convert into single-letter moves.
        moves = []
        for index in range(len(path)-1):
            moves.append(path[index].get_move(path[index+1]))
        return end - begin, num_steps, moves

class AASTERISKMisTiles(AASTERISK):
    def __init__(self, board, width) -> None:
        # self.board = board
        # self.width = width
        super().__init__(board, width)

    def run_Astar(self, start, goal):
        closedSet = set()
        cameFrom = {}

        global fScore
        fScore = collections.defaultdict(lambda: float("inf"))

        global gScore
        gScore = collections.defaultdict(lambda: float("inf"))

        gScore[start] = 0

        openHeap = [start]
        heapq.heapify(openHeap)

        fScore[start] = start.heuristic_estimate_misplaced_tiles(goal)

        while openHeap:
            current = heapq.heappop(openHeap)

            if current in closedSet:
                continue

            if current == goal:
                end = time.time()
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                #path.reverse()
                return cnt, end, path

            closedSet.add(current)

            for neighbor in current.get_neighbors(cameFrom.get(current)):
                if neighbor in closedSet:
                    continue

                tentative_gScore = gScore[current] + 1
                if tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = gScore[neighbor] + neighbor.heuristic_estimate_misplaced_tiles(goal)
                
                heapq.heappush(openHeap, neighbor)

class AASTERISKWeighMHT(AASTERISK):
    def __init__(self, board, width) -> None:
        # self.board = board
        # self.width = width
        super().__init__(board, width)

    def run_Astar(self, start, goal):
        closedSet = set()
        cameFrom = {}

        global fScore
        fScore = collections.defaultdict(lambda: float("inf"))

        global gScore
        gScore = collections.defaultdict(lambda: float("inf"))

        gScore[start] = 0

        openHeap = [start]
        heapq.heapify(openHeap)

        fScore[start] = start.heuristic_estimate_manhattan(goal)

        while openHeap:
            current = heapq.heappop(openHeap)

            if current in closedSet:
                continue

            if current == goal:
                end = time.time()
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                #path.reverse()
                return cnt, end, path

            closedSet.add(current)

            for neighbor in current.get_neighbors(cameFrom.get(current)):
                if neighbor in closedSet:
                    continue

                tentative_gScore = gScore[current] + 1
                if tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = gScore[neighbor] + 1.1 * neighbor.heuristic_estimate_manhattan(goal)
                
                heapq.heappush(openHeap, neighbor)

class AASTERISKMaxSwap(AASTERISK):
    def __init__(self, board, width) -> None:
        # self.board = board
        # self.width = width
        super().__init__(board, width)

    def run_Astar(self, start, goal):
        closedSet = set()
        cameFrom = {}

        global fScore
        fScore = collections.defaultdict(lambda: float("inf"))

        global gScore
        gScore = collections.defaultdict(lambda: float("inf"))

        gScore[start] = 0

        openHeap = [start]
        heapq.heapify(openHeap)

        fScore[start] = start.heuristic_estimate_manhattan(goal)

        while openHeap:
            current = heapq.heappop(openHeap)

            if current in closedSet:
                continue

            if current == goal:
                end = time.time()
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                #path.reverse()
                return cnt, end, path

            closedSet.add(current)

            for neighbor in current.get_neighbors(cameFrom.get(current)):
                if neighbor in closedSet:
                    continue

                tentative_gScore = gScore[current] + 1
                if tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = gScore[neighbor] + neighbor.heuristic_estimate_maxSwap(goal)
                
                heapq.heappush(openHeap, neighbor)

class AASTERISKLinearConflict(AASTERISK):
    def __init__(self, board, width) -> None:
        # self.board = board
        # self.width = width
        super().__init__(board, width)

    def run_Astar(self, start, goal):
        closedSet = set()
        cameFrom = {}

        global fScore
        fScore = collections.defaultdict(lambda: float("inf"))

        global gScore
        gScore = collections.defaultdict(lambda: float("inf"))

        gScore[start] = 0

        openHeap = [start]
        heapq.heapify(openHeap)

        fScore[start] = start.heuristic_estimate_linear_conflict(goal)

        while openHeap:
            current = heapq.heappop(openHeap)

            if current in closedSet:
                continue

            if current == goal:
                end = time.time()
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                #path.reverse()
                return cnt, end, path

            closedSet.add(current)

            for neighbor in current.get_neighbors(cameFrom.get(current)):
                if neighbor in closedSet:
                    continue

                tentative_gScore = gScore[current] + 1
                if tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = gScore[neighbor] + neighbor.heuristic_estimate_linear_conflict(goal)
                
                heapq.heappush(openHeap, neighbor)

class GreedyBestFirstSearch(AASTERISK):
    def __init__(self, board, width) -> None:
        # self.board = board
        # self.width = width
        super().__init__(board, width)

    def run_Astar(self, start, goal):
        closedSet = set()
        cameFrom = {}

        global fScore
        fScore = collections.defaultdict(lambda: float("inf"))

        global gScore
        gScore = collections.defaultdict(lambda: float("inf"))

        gScore[start] = 0

        openHeap = [start]
        heapq.heapify(openHeap)

        fScore[start] = start.heuristic_estimate_manhattan(goal)

        while openHeap:
            current = heapq.heappop(openHeap)

            if current in closedSet:
                continue

            if current == goal:
                end = time.time()
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                #path.reverse()
                return cnt, end, path

            closedSet.add(current)

            for neighbor in current.get_neighbors(cameFrom.get(current)):
                if neighbor in closedSet:
                    continue

                tentative_gScore = gScore[current] + 1
                if tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = neighbor.heuristic_estimate_manhattan(goal)
                
                heapq.heappush(openHeap, neighbor)

class GreedyLinearConflict(AASTERISK):
    def __init__(self, board, width) -> None:
        # self.board = board
        # self.width = width
        super().__init__(board, width)

    def run_Astar(self, start, goal):
        closedSet = set()
        cameFrom = {}

        global fScore
        fScore = collections.defaultdict(lambda: float("inf"))

        global gScore
        gScore = collections.defaultdict(lambda: float("inf"))

        gScore[start] = 0

        openHeap = [start]
        heapq.heapify(openHeap)

        fScore[start] = start.heuristic_estimate_linear_conflict(goal)

        while openHeap:
            current = heapq.heappop(openHeap)

            if current in closedSet:
                continue

            if current == goal:
                end = time.time()
                path = []
                path.append(current)
                cnt = 0
                step = current
                while(cameFrom.get(step)):
                    path.append(cameFrom[step])
                    step = cameFrom[step]
                    cnt = cnt + 1
                #path.reverse()
                return cnt, end, path

            closedSet.add(current)

            for neighbor in current.get_neighbors(cameFrom.get(current)):
                if neighbor in closedSet:
                    continue

                tentative_gScore = gScore[current] + 1
                if tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = neighbor.heuristic_estimate_linear_conflict(goal)
                
                heapq.heappush(openHeap, neighbor)
    
    


#### TESTING ####

# board = [[6,5,2,3],
#         [0,7,11,4],
#         [9,1,10,8],
#         [15,14,13,12]]
#print(solve(hard))

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

# board = [[9,7,5,4],
#         [6,1,0,8],
#         [10,3,14,11],
#         [13,15,2,12]]

#a = AASTERISK(board, 4)
#a = AASTERISKMisTiles(board, 4)
#a = AASTERISKWeighMHT(board, 4)
#a = AASTERISKMaxSwap(board, 4)
#a = GreedyBestFirstSearch(board, 4)
#a = GreedyLinearConflict(board, 4)
# a = AASTERISKLinearConflict(board, 4)
#duration, num_steps, moves = a.findMinimumSteps()
#print(duration, num_steps, moves)