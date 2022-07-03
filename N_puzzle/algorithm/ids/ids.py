from collections import deque
#from nodeIDS import Node
from cmath import inf
import math, time
from platform import node
import numpy as np
class IDSAgent:
    def __init__(self, cells, width) -> None:
        self.cells = cells
        self.width = width
        self.maximum_steps = 100000
        self.minimum_steps = inf
        self.minimum_steps_node = None

        self.h(self.cells)
        # i, num_cells = 0, len(self.cells)
    def h(self, cells):
        cnt = 0
        w = self.width
        for i, v in enumerate(cells, 1):
            if i == w * w:
                continue
            i1 = i % w
            i2 = (i-i1)/w + 1
            if i1 == 0:
                i1 = w
                i2 = i/w 

            v1 = v % w
            v2 = (v-v1)/w + 1
            if v1 == 0:
                v1 = w
                v2 = v/w
            cnt += abs(i1 - v1) + abs(i2 - v2)
        self.numberBeginSteps = cnt

    def findMinimumSteps(self):

        start = time.time()
        for i in range(int(self.numberBeginSteps), int(self.maximum_steps)):
            IDSstack = list([Node(cells = self.cells, width = self.width)])
            visited = set()
            while IDSstack:
                node = IDSstack.pop()
                visited.add(str(node.cells) + str(node.ordinal_step))
                node_ord_step = node.ordinal_step

                if node.isSolved():
                    if node_ord_step < self.minimum_steps:
                        self.minimum_steps = node_ord_step
                        self.minimum_steps_node = node
                    break

                if node_ord_step == i:
                    continue
                neighbors = reversed(node.getNextStates())
                for next_state, action in neighbors:
                    child = Node(cells = next_state, width = self.width, parent = node, 
                        ordinal_step = node_ord_step + 1)
                    if str(child.cells) + str(child.ordinal_step) not in visited:
                        IDSstack.append(child)
                        visited.add(str(child.cells)+ str(child.ordinal_step) )                       
            if self.minimum_steps != inf:
                # print("Number of steps: " + str(self.minimum_steps))
                break
        end = time.time()
        duration = end - start   
        return duration, self.minimum_steps #, self.minimum_steps_node.getPath()
    


class Node:
    def __init__(self, cells, width:int, parent = None, p_action = None, ordinal_step = 0, cost = 0) -> None:
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




# # cells = [1,2,0,3]
# cells = [2, 0, 3, 1, 5, 6, 4, 7, 8]
# IDS = IDSAgent(cells, math.isqrt(len(cells)))
# print(IDS.findMinimumSteps())