from collections import deque
import numpy as np

def traverse(paths, initial):
    # Stack keeps values as (path, reversed)
    print "Traversing"
    stack = deque()
    vertices = deque()
    current = initial
    reversing = False
    while current[0] != current[1] or len(stack) > 0:
        if current[0] == current[1]:
            vertices.append(current[0])
            parent, reversing = stack.pop()

            # Now skip to the next without adding parent to the stack
            if reversing:
                current = paths[parent[0]]
            else:
                current = paths[parent[1]]
        else:
            if current[2]:
                reversing = not reversing
            stack.append( (current, reversing) )

            if reversing:
                current = paths[current[1]]
            else:
                current = paths[current[0]]

    # Last one is a leaf and is not added to vertices, so add it
    vertices.append(current[0])
    return vertices

# Path:     (left, right, reversed, leftEdge, rightEdge)
# PathNode: (self, self, 0, self, self)
def amorim(G):
    allowed = [True for i in xrange(len(G))]
    n = len(G)
    edges = np.zeros((n*(n-1)/2), dtype=[('f','int16'),('t','int16'),('w','int32')] )
    e = 0
    for i in xrange(n):
        for j in xrange(i+1,n):
            edges[e] = G.getEdge(i,j)
            e = e+1
    edges.sort(order='w')
    e = 0

    # Start all paths with a single vertice
    paths = np.zeros(n*3*5, dtype="int16").reshape(n*3,5)
    for i in xrange(n):
        paths[i] = (i,i,0,i,i)
    pathSize = n
    newPath = None

    # O(|V|^2)
    while len(edges)-e > 0:
        i,j,w = edges[e] # Get the lightest edge
        e = e + 1

        # Check if any of the vertex are already in a middle of a path
        if allowed[i] and allowed[j]:
            # All O(1)
            ip = paths[i]
            jp = paths[j]
            ifirst = ip[3] == i
            jfirst = jp[3] == j
            oi = ip[4] if ifirst else ip[3]
            oj = jp[4] if jfirst else jp[3]

            if oi == j or oj == i:
                continue

            # If their paths are bigger than 1 disallow them
            if paths[i][0] != i:
                allowed[i] = False
            if paths[j][0] != j:
                allowed[j] = False

            # Join both paths
            newPath = (n, n+1, 0, 0, 0)
            paths[n] = ip
            paths[n+1] = jp
            if not ifirst and jfirst:
                newPath = (n, n+1, 0, ip[3], jp[4])
                # newPath = Path(ip,jp)
            elif ifirst and jfirst:
                newPath = (n, n+1, 0, ip[4], jp[4])
                paths[n][2] = not paths[n][2]
                # newPath = Path(ip.reverse(),jp)
            elif ifirst and not jfirst:
                newPath = (n+1, n, 0, jp[3], ip[4])
                # newPath = Path(jp,ip)
            else:
                newPath = (n, n+1, 0, ip[3], jp[3])
                paths[n+1][2] = not paths[n][2]
                # newPath = Path(ip,jp.reverse())

            # O(1)
            paths[i] = newPath
            paths[j] = newPath
            paths[oi] = newPath
            paths[oj] = newPath
            n = n+2

    # O(|V|^2) given that max depth is |E|
    return list(traverse(paths,newPath))
