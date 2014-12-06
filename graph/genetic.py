import random
from math import ceil, log10
from cartesian_graph import CartesianGraph

class Path:
    def __init__(self,G,vertices):
        self.graph = G
        self.vertices = vertices
        self.cost = G.pathCost(vertices)
    
    def mutate(self):
        p = [i for i in self.vertices]
        n = random.randrange(1,ceil(len(p)**0.3))
        for i in range(n):
            a = random.randrange(0,len(p))
            b = random.randrange(0,len(p))
            p[a], p[b] = p[b], p[a]
        return Path(self.graph, p)
    
    def crossOver(self,other):
        size = len(self.vertices)
        intersect = random.randrange(0, size)
        remaining = set(range(size))
        
        # Keeps the position of duplicate items
        duplicate = list()
        child = list()
            
        for v in self.vertices[:intersect] + other.vertices[intersect:]:
            if v in remaining:
                duplicate.append(len(child))
            else:
                remaining.discard(v)
            child.append(v)
            
        for v in list(remaining):
            child[duplicate.pop()] = v
            
        return Path(self.graph,child)

class Population:
    def __init__(self, G, paths):
        self.graph = G
        self.paths = self.sortPath(paths)
    
    def sortPath(self, path):
        return sorted(path, key=lambda x: x.cost)

    def bestVertices(self):
        return self.bestPath().vertices

    def bestPath(self):
        return self.paths[0]
        
    # Natural Selection for a list of individuals
    def select(self,unsorted_individuals):
        individuals = self.sortPath(unsorted_individuals)
        size = len(individuals)
        
        ten_p = int(ceil(len(self.paths)/10))
        mediocre_bottom = int(ceil(size*0.6))
        # We should fix some numbers instead of using percentage.
        best = individuals[:ten_p*5]
        mediocre = individuals[mediocre_bottom:mediocre_bottom+ten_p*3]
        worst = individuals[ten_p*(-2):]
        
        return best + mediocre + worst
    
    # Mutate, CrossOver and Select next generation.
    def nextGeneration(self):
        mutations = map(lambda x: x.mutate(), self.paths)
        children = map(
            lambda x,y: [x.crossOver(y), y.crossOver(x)],
            self.paths[:-1], 
            self.paths[1:])
        
        children = [ i for it in children for i in it ]
        
        everyone = self.paths + mutations + children
        return Population(self.graph, self.select(everyone))

def generatePopulation(G, size=100, randomFactor=0.5):
    randomSize = int(size*randomFactor)
    nearestSize = size-randomSize
    return Population(G,
        generateRandomPaths(G, randomSize) +
        generateNeighborsPaths(G,nearestSize)
    )

# Completely Random
def generateRandomPaths(G, popSize):
    return [ generateRandomPath(G) for i in range(popSize) ]

def generateRandomPath(G):
    indexes = range(len(G))
    random.shuffle(indexes)
    return Path(G,indexes)

def generateNearestNeighbors(G):
    return [
        map(
            lambda (x,y,w): y,
            sorted(G.getEdges(i), key= lambda e: e[2])
        ) for i in range(0,len(G))
    ]

def generateNeighborsPaths(G, size):
    neighbors = generateNearestNeighbors(G)
    return [ generateNeighborsPath(G,neighbors) for i in range(size) ]

def generateNeighborsPath(G, nearestNeighbors=None):
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

    return Path(G,path)

def improveCost(G,vs,i):
    return G.getEdge(vs[i],vs[i+1])[2] - G.getEdge(vs[-1], vs[i])[2]

def improvedPath(G,vs,i):
    return Path(G,vs[:i+1]+vs[-2:-1]+vs[i+1:][::-1])

def improvePath(G,path,alpha=100,depth=0,r=set()):
    vs = path.vertices
    if depth < alpha:
        for i, x in enumerate(vs[1:-2]):
            if x in r:
                continue
            c = improveCost(G,vs,i)
            if c > 0:
                print "c>0"
                newPath = improvedPath(G,vs,i)
                if newPath.cost < path.cost:
                    return newPath
                else:
                    return improvePath(G, newPath, alpha, depth+1, r.union([x]))
        else:
            weigths = map(lambda i: (i, improveCost(G,vs,i)), range(1,len(vs)-1))
            best = sorted(weigths, key=lambda (i, c): c)[-1]
            if best[1] > 0:
                newPath = improvedPath(G,vs,best[0])
                if newPath.cost < path.cost:
                    return newPath
                else:
                    return improvePath(G, newPath, alpha, depth+1, r.union([x]))
    if depth == 0:
        return path
