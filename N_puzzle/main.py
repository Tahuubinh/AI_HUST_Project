from environment import Environment
from agents.bfs import BFSAgent
import time
N = 2
#cells = [1, 2, 3, 0]
cells = [3, 1, 2, 0]

env = Environment(width = N, cells = cells)
bfs_agent = BFSAgent(env)

start = time.time()
ans, path = bfs_agent.findMinimumSteps()
print(ans)
print(path)
end = time.time()
print(end - start)

# start = time.time()
# a = 0
# for i in range(10000):
#     a = a + 1
# end = time.time()
# print(end - start)
# ans = bfs_agent.solve()
# print(ans)
# for path in reversed(ans):
# 		soln = ''
# 		for elem in path:
# 			soln += str(elem)+' '
# 		print(soln)