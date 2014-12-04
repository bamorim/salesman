import random
from math import ceil
from cartesian_graph import CartesianGraph

class Path:
    def __init__(self,G,vertices):
        self.graph = G
        self.vertices = vertices
        self.cost = reduce(lambda acc,edge: acc + edge[2], G.pathEdges(vertices+ [vertices[0]] ), 0)
    
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
        self.paths = paths
    
    def bestVertices(self):
        return sorted(self.paths, key=lambda x: x.cost)[0].vertices
        
    # Natural Selection for a list of individuals
    def select(self,unsorted_individuals):
        individuals = sorted(unsorted_individuals, key=lambda x: x.cost)
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


def generatePopulation(G, size):
    paths = []
    n = len(G)
    indexes = range(n)
    for each in range(size):
        x = indexes[:]
        random.shuffle(x)
        paths.append(Path(G,x))
    return Population(G,paths)


def run(G, iters, popsize):
    pop = generatePopulation(G, popsize)
    for i in range(iters):
        pop = pop.nextGeneration()
    return pop