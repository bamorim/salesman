import numpy as np
from math import floor

def improvePath(G,initial_path):
    path = np.array(initial_path,dtype="int16")
    improved = True

    while improved:
        improved = False
        for i in xrange(0,len(G)):
            for j in xrange(i+2,len(G)):
                a = path[i]
                b = path[i-1]
                c = path[j]
                d = path[j-1]
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
                if aSide != bSide and cSide != dSide:
                    path[i:j] = path[i:j][::-1]
                    improved = True
                    yield path
                    break
