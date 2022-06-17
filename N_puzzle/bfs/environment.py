from node import Node

class Environment:
    def __init__(self, width:int, cells:list) -> None:
        self.width = width
        self.cells = cells
        self.size = self.width * self.width
        self.goal = self.getGoal()

    def copy(self):
        clone_cells = list()
        for cell in self.cells:
            clone_cells.append(cell)
        return clone_cells

    def swapCell(self, r:int, c:int, i:int, j:int):
        clone_cells = self.copy()
        
        clone_cells[r * self.width + c], clone_cells[i * self.width + j] \
                = clone_cells[i * self.width + j], clone_cells[r * self.width + c]
        return clone_cells

    def getGoal(self):
        goal = list()
        for i in range(1, self.size):
            goal.append(i)
        goal.append(0)
        return goal

    def isSolved(self):
        return self.cells == self.goal

    def getMoves(self):
        empty_space = self.cells.index(0)
        empty_space_row = empty_space // self.width
        empty_space_col = empty_space % self.width
        moves = list()

        actions = {"R":(empty_space_row, empty_space_col + 1),
                             "L":(empty_space_row, empty_space_col - 1),
                             "U":(empty_space_row - 1, empty_space_col),
                             "D":(empty_space_row + 1, empty_space_col)}

        for action, (row, col) in actions.items():
            if row >= 0 and row < self.width and \
             col >= 0 and col < self.width:
                move = self.swapCell(empty_space_row, empty_space_col, row, col), action
                moves.append(move)
        
        return moves
