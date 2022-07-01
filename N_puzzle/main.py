from algorithm.Uniformed.Uninformed_search import BFSAgent
import math

cells = [8,5,1,
		6,7,0,
		3,2,4]
cells = [6,5,2,3,
        0,7,11,4,
        9,1,10,8,
        15,14,13,12]
bfs = BFSAgent(cells, math.isqrt(len(cells)))
time, num_steps = bfs.findMinimumSteps()
print(time)
print(num_steps)
