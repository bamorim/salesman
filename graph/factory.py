from cartesian_graph import CartesianGraph

def makeGraph(path):
    G = CartesianGraph()
    with open(path,'r') as f:
        n = f.readline()
        for line in f.readlines():
            x,y = map(lambda k: int(k), line.split(' '))
            G.add(x,y)
    return G