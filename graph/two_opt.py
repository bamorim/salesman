def improvePath(G,initial_path):
    path = initial_path
    cost = G.pathCost(path)
    edgeCost = lambda a,b: G.getEdge(a,b)[2]
    while improved:
        improved = False
        for i in range(0,len(G)):
            for j in range(i+1,len(G)):
                newPath = swap2op(path,i,j)
                costDiff = edgeCost( path[i], path[j-1]) + edgeCost( path[i-1], path[j] ) - edgeCost( path[i], path[i-1] ) - edgeCost( path[j], path[j-1] )
                if costDiff < 0:
                    path = newPath
                    improved = True
                    break
    return path

def swap2op(path,i,j):
    return path[:i] + path[i:j][::-1] + path[j:]
