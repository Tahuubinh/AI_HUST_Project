from collections import deque
#from nodeBFS import Node
from cmath import inf
import math, time
import numpy as np

class BFSAgent:
    def __init__(self, cells, width) -> None:
        self.cells = cells
        self.width = width
        self.minimum_steps = inf
        self.minimum_steps_node = None

    def findMinimumSteps(self):
        start = time.time()
        BFSqueue = deque([Node(cells = self.cells, width = self.width)])
        # if using list, error: unhashable type: 'list'
        visited = set()
        visited.add(str(BFSqueue[0].cells))

        while BFSqueue:
            node = BFSqueue.pop()
            node_ord_step = node.ordinal_step
            if node.isSolved():
                if node_ord_step < self.minimum_steps:
                    self.minimum_steps = node_ord_step
                    self.minimum_steps_node = node
            for next_state, action in node.getNextStates():
                child = Node(cells = next_state, width = self.width, parent = node, 
                    ordinal_step = node_ord_step + 1)
                if str(child.cells) not in visited:
                    BFSqueue.appendleft(child)
                    visited.add(str(child.cells))

        end = time.time()
        duration = end - start
        return duration, self.minimum_steps #, self.minimum_steps_node.getPath()

class Node:
    def __init__(self, cells, width:int, parent = None, p_action = None, ordinal_step = 0) -> None:
        self.cells = cells
        self.parent = parent
        self.p_action = p_action
        self.ordinal_step = ordinal_step
        self.width = int(width)

    def isSolved(self):
        i, num_cells = 0, len(self.cells)
        for i, v in enumerate(self.cells, 1):
            if (i != v):
                break
        if i == num_cells:
            return True
        return False

    def swapCell(self, r:int, c:int, i:int, j:int):
        clone_cells = list(self.cells)
        #print(self.cells)
        
        #print(r, c, i, j)
        clone_cells[r * self.width + c], clone_cells[i * self.width + j] \
                    = clone_cells[i * self.width + j], clone_cells[r * self.width + c]
        return clone_cells

    def getNextStates(self):
        empty_space = self.cells.index(0)
        empty_space_row = empty_space // self.width
        empty_space_col = empty_space % self.width
        next_states = list()

        actions = {"R":(empty_space_row, empty_space_col + 1),
                             "L":(empty_space_row, empty_space_col - 1),
                             "U":(empty_space_row - 1, empty_space_col),
                             "D":(empty_space_row + 1, empty_space_col)}

        for action, (row, col) in actions.items():
            if row >= 0 and row < self.width and col >= 0 and col < self.width:
                #print(self.width, empty_space_row, empty_space_col, row, col)
                move = self.swapCell(empty_space_row, empty_space_col, row, col), action
                next_states.append(move)
        
        #print(next_states)
        return next_states




# cells = [1,2,0,3]
# cells = [3, 4, 0, 1, 8, 2, 7, 5, 6]
# BFS = BFSAgent(cells, math.isqrt(len(cells)))
# print(BFS.findMinimumSteps())