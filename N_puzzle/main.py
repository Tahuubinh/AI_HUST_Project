from environment import Environment
from agents.bfs import BFSAgent
N = 2
#cells = [1, 2, 3, 0]
cells = [3, 1, 2, 0]

env = Environment(width = N, cells = cells)
bfs_agent = BFSAgent(env)
ans, path = bfs_agent.findMinimumSteps()
print(ans)
print(path)
# ans = bfs_agent.solve()
# print(ans)
# for path in reversed(ans):
# 		soln = ''
# 		for elem in path:
# 			soln += str(elem)+' '
# 		print(soln)