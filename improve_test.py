from salesman.graph.factory import makeGraph
from salesman.graph.genetic import improvePath
from salesman.graph.genetic import generateNeighborsPaths

g = makeGraph("./points-500.txt")
[path] = generateNeighborsPaths(g,1)
path = improvePath(g,path,len(g))
