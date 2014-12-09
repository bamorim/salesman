import random, sys, math
import numpy as np
from factory import makeGraph
import plot as gplot

class DisjointSet:
	def __init__(self, List):
		self.nodes = [{i} for i in List]

	def find(self, x):
		for index, node in enumerate(self.nodes):
			if x in node:
				return index
		return -1

	def union(self, x, y):
		a, b = self.find(x), self.find(y)
		if a == b or a*b < 0:
			return None
		self.nodes[a].update(self.nodes[b])
		self.nodes.pop(b)

	def __iter__(self):
		return iter(self.nodes)
	def __len__(self):
		return len(self.nodes)
	def __repr__(self):
		return str(self.nodes)

class MinimumSpanningTree:
	def __init__(self, n):
		self.vertices = [[] for each in range(n)]
		self.length = n

	def addEdge(self,i,j):
		self.vertices[i].append(j)
		self.vertices[j].append(i)

	def __getitem__(self, key):
		return self.vertices[key]

	def __len__(self):
		return self.length

	def __repr__(self):
		return str(self.vertices)


def MST(G):
	#Boruvka's algorithm
	n = len(G)
	#initialize forest
	T = DisjointSet(range(n))
	SpTree = MinimumSpanningTree(n)
	#While forest T has more than one component
	while len(T) > 1:
		#For each component C of T
		for C in T:
		#Initialize an empty set S of edges
			S = set()
			#For each vertex v in C
			for v in C:
				#Find the cheapest edge from v to a vertex >>outside<< of C
				validEdges = [e for e in G.getEdges(v) if e[1] not in C]
				cheapest = min(validEdges, key = lambda t: t[2])
				#Add it to S
				S.add(cheapest)
			#Add the cheapest edge in S to T
			cheapest = min(S, key = lambda t: t[2])
			v1, v2, w = cheapest
			#Merge components in T
			T.union(v1,v2)
			SpTree.addEdge(v1,v2)
	return SpTree

def DFS(Tree):
	#Returns a path
	path, S, n = [], [], len(Tree)
	discovered = [False for i in range(n)]
	vertex = random.randrange(n)

	S.append(vertex)
	#While S isnt empty
	while S:
		v = S.pop()
		if not discovered[v]:
			discovered[v] = True
			path.append(v)
			for u in Tree[v]:
				S.append(u)
	return path