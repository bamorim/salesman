def improvePath(G,initial_path):
    path = initial_path
    cost = G.pathCost(path)
    edgeCost = lambda a,b: G.getEdge(a,b)[2]
    for i in xrange(0,len(G)):
        for j in xrange(i+2,len(G)):
            if crosses(G,path[i],path[i-1],path[j],path[j-1]):
                swap2op(path,i,j)
                return True
    return False

# Check if a-b crosses with c-d
def crosses(G,a,b,c,d):
    ax, ay = G[a]
    bx, by = G[b]
    cx, cy = G[c]
    dx, dy = G[d]

    aSide = (dx - cx) * (ay - cy) - (dy - cy) * (ax - cx) > 0;
    bSide = (dx - cx) * (by - cy) - (dy - cy) * (bx - cx) > 0;
    cSide = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax) > 0;
    dSide = (bx - ax) * (dy - ay) - (by - ay) * (dx - ax) > 0;

    # a and b should be on different sides of CD rect
    # same must be true for c and d and AB rect
    return aSide != bSide and cSide != dSide

def swapCost(G,path,i,j):
    # Old edges
    ii1 = G.getEdge( path[i], path[i-1] )[2]
    jj1 = G.getEdge( path[j], path[j-1] )[2]

    # New edges
    ij = G.getEdge( path[i], path[j] )[2]
    i1j1 = G.getEdge( path[i-1], path[j-1] )[2]
    return ij + i1j1 - ii1 - jj1

# In place swap for performance
def swap2op(path,i,j):
    path[i:j] = path[i:j][::-1]
