from collections import deque
class PathNode:
    def __init__(self,value):
        self.value = value
        self.leftEdge = value
        self.rightEdge = value

    def reverse(self):
        return self

class Path:
    def __init__(self, left, right, reverse=False):
        self.left = left
        self.right = right
        self.reversed = reverse
        if reverse:
            self.leftEdge = right.rightEdge
            self.rightEdge = left.leftEdge
        else:
            self.leftEdge = left.leftEdge
            self.rightEdge = right.rightEdge

    def reverse(self):
        return Path(self.left, self.right, not self.reversed)

    def traverse(self):
        # Stack keeps values as (path, reversed)
        stack = deque()
        vertices = deque()
        current = self
        reversing = False
        while current.__class__ != PathNode or len(stack) > 0:
            if current.__class__ == PathNode:
                vertices.append(current.value)
                parent, reversing = stack.pop()

                # Now skip to the next without adding parent to the stack
                if reversing:
                    current = parent.left
                else:
                    current = parent.right
            else:
                if current.reversed:
                    reversing = not reversing
                stack.append( (current, reversing) )
                if reversing:
                    current = current.right
                else:
                    current = current.left

        # Last one is a leaf and is not added to vertices, so add it
        vertices.append(current.value)
        return vertices

def amorim(G):
    allowed = [True for i in range(len(G))]
    edges = [G.getEdge(i,j) for i in range(len(G)) for j in range(len(G)) if i != j]
    edges.sort(key= lambda e: e[2])

    # Start all paths with a single vertice
    paths = [PathNode(i) for i in range(len(G))]
    newPath = None

    while len(edges) > 0:
        i,j,w = edges.pop(0) # Get the lightest edge

        # Check if any of the vertex are already in a middle of a path
        if allowed[i] and allowed[j]:
            ip = paths[i]
            jp = paths[j]
            ifirst = ip.leftEdge == i
            jfirst = jp.leftEdge == j
            oi = ip.rightEdge if ifirst else ip.leftEdge
            oj = jp.rightEdge if jfirst else jp.leftEdge

            if oi == j or oj == i:
                continue

            # If their paths are bigger than 1 disallow them
            if paths[i].__class__ != PathNode:
                allowed[i] = False
            if paths[j].__class__ != PathNode:
                allowed[j] = False

            # Join both paths
            if not ifirst and jfirst:
                newPath = Path(ip,jp)
            elif ifirst and jfirst:
                newPath = Path(ip.reverse(),jp)
            elif ifirst and not jfirst:
                newPath = Path(jp,ip)
            else:
                newPath = Path(ip,jp.reverse())

            paths[i] = newPath
            paths[j] = newPath
            paths[oi] = newPath
            paths[oj] = newPath

    return list(newPath.traverse())
