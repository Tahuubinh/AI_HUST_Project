import math
import heapq
import collections
import copy

# For each node, the total cost of getting from the start node to the goal
# by passing by that node. That value is partly known, partly heuristic.
fScore = collections.defaultdict(lambda: float("inf"))

# class Block_Puzzle:
#     def __init__(self, blocks):
#         self.blocks = blocks

#         self.fScore = blocks[0]

#     def __eq__(self, other):

#         if other == None:
#             return False
#         return self.blocks == other.blocks

#     def __lt__(self, other):
#         if other == None:
#             return False
#         return self.fScore < other.fScore

#     def __hash__(self):
#         return hash(frozenset(self.blocks))

# a = Block_Puzzle([9, 3, 1, 2])
# b = Block_Puzzle([5, 2, 3, 5])

# li = [a, b]
# heapq.heappush(li,Block_Puzzle([2, 3]))
 
# # using heapify to convert list into heap
# heapq.heapify(li)
# x = heapq.heappop(li)

# #print(x.blocks)
# a = set([Block_Puzzle([2, 3])])
# a.add(Block_Puzzle([2, 3]))
# print(Block_Puzzle([2, 3]) in a)

# class Item(object):
#   def __init__(self, foo, bar):
#     self.foo = foo
#     self.bar = bar
#   def __repr__(self):
#     return "Item(%s, %s)" % (self.foo, self.bar)
#   def __eq__(self, other):
#     if isinstance(other, Item):
#       return ((self.foo == other.foo) and (self.bar == other.bar))
#     else:
#       return False
#   def __ne__(self, other):
#     return (not self.__eq__(other))

# a = set([Item(1,2), Item(1,2)])
# print(a)

class A(object):
    def add(a, b):
        return a + b

a = A()
print(A.add(1, 2))
