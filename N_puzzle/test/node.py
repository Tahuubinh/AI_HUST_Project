class Node:
    def __init__(self, env, parent = None, p_action = None, ordinal_step = 0) -> None:
        self.env = env
        self.parent = parent
        self.o_action = p_action
        self.ordinal_step = ordinal_step

    def getState(self):
        return self.env.cells

    def getPath(self):
        node = self
        path = list()
        while node:
            path.append(node.getState())
            node = node.parent
        return path

    def isSolved(self):
        return self.env.isSolved()

    def getMoves(self):
        return self.env.getMoves()