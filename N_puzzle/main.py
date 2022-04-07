from environment import Environment
from BFSAgent import BFSAgent
N = 2
cells = [1, 2, 0, 3]

env = Environment(width = N, cells = cells)
bfs_agent = BFSAgent(env)
ans = bfs_agent.solve()
print(ans)
for path in reversed(ans):
		soln = ''
		for elem in path:
			soln += str(elem)+' '
		print(soln)