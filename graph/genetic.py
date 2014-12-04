import random
from math import ceil
from cartesian_graph import CartesianGraph

class Path:
    def __init__(self,G,vertices):
        self.graph = G
        self.vertices = vertices
        self.cost = reduce(lambda acc,edge: acc + edge[2], G.pathEdges(vertices), 0)
    
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
        remaining = set(range(size))
        intersect = random.randrange(0, size)
        
        child = [i for i in self.vertices[:intersect]]
        for i in self.vertices[:intersect]:
            remaining.remove(i)
            child.append(i)
            
        for each in remaining:
            child.append(i)

class Population:
    def __init__(self, G, paths):
        self.graph = G
        self.paths = self.sort(paths)
    
    def sort(self,paths):
        sorted(paths, key=lambda x: x.cost)
        
    def survivors(self):
        size = len(self.paths)
        
        best = self.paths[:ceil(size*0.4)]
        mediocre = self.paths[ceil(size*0.65):ceil(size*0.85)]
        worst = self.paths[ceil(size*0.9):]
        
        return best + mediocre + worst
    
    def nextGeneration(self):
        survivors = self.survivors()
        
        mutations = map(lambda x: x.mutate(), survivors)
        return Population(G, survivors + mutations)


def generatePopulation(G, size):
    paths = []
    n = G.size()
    indexes = range(n)
    for each in range(size):
        paths.append(Path(G,random.sort(indexes)))
    return Population(G,paths)


def run(G, iters, popsize):
    pop = generatePopulation(G, popsize)
    for i in range(iters):
        pop = nextGeneration(G, pop)
    return sortPopulation(G, pop)[0]