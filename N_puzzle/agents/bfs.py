from collections import deque
from node import Node
from environment import Environment
from cmath import inf

class BFSAgent:
    def __init__(self, env) -> None:
        self.env = env
        self.width = env.width

    def solve(self):
        cells = self.env.cells
        BFSqueue = deque([Node(self.env)])

        # if using list, error: unhashable type: 'list'
        visited = set()
        visited.add(str(BFSqueue[0].getState()))

        while BFSqueue:
            node = BFSqueue.pop()
            if node.isSolved():
                return node.getPath()
            for move, action in node.getMoves():
                child = Node(Environment(self.width, move), node, action)
                if str(child.getState()) not in visited:
                    BFSqueue.appendleft(child)
                    visited.add(str(child.getState()))

