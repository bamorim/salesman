
def BruteForce(points):
    def dist(X,Y):
        return ((X[0]-Y[0])**2 + (X[1]-Y[1])**2)**0.5
    
    def cost(path):
        cst = 0
        for index, point in enumerate(path):
            if index == len(path)-1:
                return cst
            cst += dist(path[index],path[index+1)]
            
    n = len(points)
    permutations = [[points[i-j] for i in range(n)] for j in range(n)]
    
    best = permutations[0]
    
    for path in permutations:
        if cost(path) > cost(best):
            best = path
    
    return best