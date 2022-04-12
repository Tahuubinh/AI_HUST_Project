from collections import deque
from node import Node
from environment import Environment
from cmath import inf

class BFSAgent:
    def __init__(self, env) -> None:
        self.env = env
        self.width = env.width
        self.minimum_steps = inf
        self.minimum_steps_node = None

    def solve(self):
        cells = self.env.cells
        BFSqueue = deque([Node(env = self.env)])

        # if using list, error: unhashable type: 'list'
        visited = set()
        visited.add(str(BFSqueue[0].getState()))

        while BFSqueue:
            node = BFSqueue.pop()
            if node.isSolved():
                return node.getPath()
            for move, action in node.getMoves():
                child = Node(env = Environment(self.width, move), parent = node, p_action = action)
                if str(child.getState()) not in visited:
                    BFSqueue.appendleft(child)
                    visited.add(str(child.getState()))

    def findMinimumSteps(self):
        cells = self.env.cells
        BFSqueue = deque([Node(env = self.env)])

        # if using list, error: unhashable type: 'list'
        visited = set()
        visited.add(str(BFSqueue[0].getState()))

        while BFSqueue:
            node = BFSqueue.pop()
            node_ord_step = node.ordinal_step
            if node.isSolved():
                if node_ord_step < self.minimum_steps:
                    self.minimum_steps = node_ord_step
                    self.minimum_steps_node = node
            for move, action in node.getMoves():
                child = Node(env = Environment(self.width, move), parent = node, p_action = action, 
                    ordinal_step = node_ord_step + 1)
                if str(child.getState()) not in visited:
                    BFSqueue.appendleft(child)
                    visited.add(str(child.getState()))

        return self.minimum_steps, self.minimum_steps_node.getPath()

