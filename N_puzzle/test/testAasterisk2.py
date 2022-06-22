import heapq
from random import shuffle
import math


n=3
fBoard = [1,2,3,
          4,5,6,
          7,8,0]

board = [1,7,3,
         4,5,6,
         8,0,2]
board = [0,3,1,
         4,2,6,
         7,5,8]
board = [0,1,3,
         4,2,6,
         7,5,8]


class Board():

    def __init__(self,boardList,cost,parent):
        self.boardList = boardList
        self.heuristic = calcHeuristic(self.boardList)
        self.cost = cost
        self.totalCost = self.cost + self.heuristic
        self.parent = parent

    def __hash__(self):
        return hash(frozenset(self.boardList))

    def __lt__(self, other):
        return self.totalCost < other.totalCost

def aStar():
    cost = {}
    start = Board(board,0,None)
    open_list = [start]
    heapq.heapify(open_list)
    closed_list  = set([])
    end = Board(fBoard,99,None)
    while open_list:
        tmp_board = heapq.heappop(open_list)
        current_board = tmp_board.boardList
        if tmp_board.heuristic == 0:
            end = tmp_board
            break

        index = current_board.index(0)
        x = int(index // 3)
        y = int(index % 3)
        listOfMoves = checkMove(x,y)

        
        for move in listOfMoves:
            moveBoard = current_board[:]
            moveIndex = move[0]*3 + move[1]
            moveBoard[index],moveBoard[moveIndex] = moveBoard[moveIndex],moveBoard[index]
            newBoard = Board(moveBoard,None,None)
            if newBoard not in open_list and newBoard not in closed_list:
                open_list.add(newBoard)
                newBoard.parent = moveBoard
                newBoard.cost = moveBoard.cost + 1
            else:
                if 
            # new_cost = newBoard.totalCost
            # if newBoard not in closed_list  or new_cost < cost[newBoard]:
            #     cost[newBoard] = new_cost
            #     closed_list.add(newBoard)
            #     newBoard.parent = tmp_board
            #     heapq.heappush(open_list,newBoard)

    var = end
    cnt = 0
    while var != start:
        cnt = cnt + 1
        var = var.parent
    print(cnt)

# def aStar():
#     pq = []
#     cost = {}
#     visited = {}
#     start = Board(board,0,None)
#     end = Board(fBoard,99,None)
#     heapq.heappush(pq,start)
#     while pq:
#         tmp_board = heapq.heappop(pq)
#         if tmp_board.heuristic == 0:
#             end = tmp_board
#             break

#         index = tmp_board.boardList.index(0)
#         x = int(index // 3)
#         y = int(index % 3)
#         listOfMoves = checkMove(x,y)

#         for move in listOfMoves:
#             moveBoard = tmp_board.boardList[:]
#             moveIndex = move[0]*3 + move[1]
#             moveBoard[index],moveBoard[moveIndex] = moveBoard[moveIndex],moveBoard[index]
#             newBoard = Board(moveBoard,tmp_board.cost+1,tmp_board)
#             new_cost = newBoard.totalCost
#             if newBoard not in visited or new_cost < cost[newBoard]:
#                 cost[newBoard] = new_cost
#                 visited[newBoard] = 1
#                 newBoard.parent = tmp_board
#                 heapq.heappush(pq,newBoard)

#     var = end
#     cnt = 0
#     while var != start:
#         cnt = cnt + 1
#         var = var.parent
#     print(cnt)

# def manhattanDist(index,element):
#     idx = fBoard.index(element)
#     manhattan = 0
#     fBoard_x = idx/3
#     fBoard_y = idx%3
#     x = index/3
#     y = index%3
#     manhattan += math.fabs(x-fBoard_x)
#     manhattan += math.fabs(y-fBoard_y)
#     return manhattan

# def calcHeuristic(boardList):
#     heuristic = 0
#     for var in boardList:
#         x = var//3
#         y = var%3
#         # if fBoard.index(var) != boardList.index(var):
#         #     heuristic+=1
#         heuristic+=manhattanDist(boardList.index(var),var)
#     return heuristic

def calcHeuristic(boardList):
    heuristic = 0
    for index, val in enumerate(boardList):
        x_index = index // 3
        y_index = index % 3
        if val == 0:
            val = 8
        else:
            val = val - 1
        x_val = val // 3
        y_val = val % 3
        heuristic += math.fabs(x_index - x_val) + math.fabs(y_index - y_val)
    return heuristic

def checkMove(x,y):
    listOfMoves = [[x,y]]
    if(x+1<n):
        listOfMoves.append([x+1,y])
    if(x-1>=0):
        listOfMoves.append([x-1,y])
    if(y-1>=0):
        listOfMoves.append([x,y-1])
    if(y+1<n):
        listOfMoves.append([x,y+1])

    return listOfMoves

# a = [0, 1, 3, 4, 2, 6, 7, 5, 8]
# a = [1, 2, 3, 4, 5, 6, 7, 0, 8]
# print(calcHeuristic(a))
# print(calcHeuristic2(a))
aStar()