import threading, queue, random

#NOT WORKING YET !!!

def pointerJump(parents):
	sucessor = [None for each in parents]
	sucessor_next = [None for each in parents]
	n = len(parents)

	for i in range(n):
		#Do in parallel
		sucessor[i] = parents[i]

	while True:
		for i in range(n):
			#Do in parallel
			sucessor_next[i] = sucessor[sucessor[i]]

		if sucessor_next == sucessor:
			break
		for i in range(n):
			sucessor[i] = sucessor_next[i]
	return sucessor

def superVertexPointerJumping(S):
	if len(S) > 2:
		threadlist = []
		#Set of the supervertices plus the root
		SV = set()
		for v in S:
			if random.random() < 0.5:
				#Make v a supervertex
				pass
		
		t = threading.Thread(target = superVertexPointerJumping, args = (S-SV,))
		t.start()

		for u in SV:
			#perform one pointer jump in u
			pass

		for x in S - SV:
			#perform one pointer jump in x
			pass


		

