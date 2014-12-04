import numpy as np

class CartesianGraph:
    def __init__(self):
        self.vertices = []
        
    # Complexity: O(1)
    def add(self,x,y):
        self.vertices.append((x,y))
        return len(self.vertices)-1
        
    # Complexity: O(1)
    def __getitem__(self, key):
        return self.vertices[key]
    
    # Complexity: O(1)
    def getEdge(self,v1,v2):
        x1, y1 = self.vertices[v1]
        x2, y2 = self.vertices[v2]
        weight = ((x1-x2)**2 + (y1-y2)**2)**0.5
        return (v1,v2,weight)
    
    # Complexity: O(n)
    def getEdges(self,v1):
        return [self.getEdge(v1,i) for i in range(len(self.vertices)) if i != v1]
    
    # Complexity: O(len(path))
    def pathEdges(self,path):
        return map(lambda f,t: self.getEdge(f,t), path[:-1], path[1:])
        
    # Complexity O(1)
    def __len__(self):
        return len(self.vertices)