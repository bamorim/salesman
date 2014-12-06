def amorim(G):
    allowed = [True for i in range(len(G))]
    edges = [G.getEdge(i,j) for i in range(len(G)) for j in range(len(G)) if i != j]
    edges.sort(key= lambda e: e[2])

    # Start all paths with a single vertice
    paths = [[i] for i in range(len(G))]
    newPath = []

    while len(edges) > 0:
        i,j,w = edges.pop(0) # Get the lightest edge

        # Check if any of the vertex are already in a middle of a path
        if allowed[i] and allowed[j]:
            ip = paths[i]
            jp = paths[j]
            ifirst = ip[0] == i
            jfirst = jp[0] == j
            oi = paths[i][ -1 if ifirst else 0 ]
            oj = paths[j][ -1 if jfirst else 0 ]

            if oi == j or oj == i:
                continue

            # If their paths are bigger than 1 disallow them
            if len(paths[i]) > 1:
                allowed[i] = False
            if len(paths[j]) > 1:
                allowed[j] = False

            # Join both paths
            newPath = paths[i]+paths[j]
            if not ifirst and jfirst:
                newPath = ip + jp
            elif ifirst and jfirst:
                newPath = ip[::-1]+jp
            elif ifirst and not jfirst:
                newPath = jp + ip
            else:
                newPath = ip + jp[::-1]

            paths[i] = newPath
            paths[j] = newPath
            paths[oi] = newPath
            paths[oj] = newPath

    return newPath
