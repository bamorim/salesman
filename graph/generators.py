import random

def generateRandomPath(G):
    indexes = range(len(G))
    random.shuffle(indexes)
    return indexes

def generateNearestNeighbors(G):
    return [
        map(
            lambda (x,y,w): y,
            sorted(G.getEdges(i), key= lambda e: e[2])
        ) for i in range(0,len(G))
    ]

def generateNeighborsPath(G, nearestNeighbors=None,nearestMax=3):
    if nearestNeighbors==None:
        nearestNeighbors = generateNearestNeighbors(G)
    init = random.randrange(0,len(G))
    nearestMax = 3
    path = [ init ]
    included = [ True if i == init else False for i in range(len(G)) ]

    for i in range(1,len(G)):
        nextVertex = filter( lambda v: not included[v], nearestNeighbors[path[i-1]] )[
            random.randrange(0, nearestMax if len(G) - i > nearestMax else len(G) - i)
        ]
        path.append(nextVertex)
        included[nextVertex] = True

    return path
