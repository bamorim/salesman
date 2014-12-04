#!/usr/bin/env python

import sys, math

def plot(g, population, fname):
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt
    plt.close('all')
    
    mult = 2**math.floor( math.log10( len(g.vertices) ) )
    fig = plt.figure(1, figsize=(2*mult, 2*mult))
    
    [i.set_linewidth(0.1) for i in plt.gca().spines.itervalues()]
    
    gplot.plotVertices(plt, g)
    gplot.plotPath(plt,g,population.bestVertices())
    
    #plt.xlim(0,plt.xlim()[1]/1.2)
    #plt.ylim(0,plt.ylim()[1]/1.2)
    
    fig.savefig(fname+".png", bbox_inches='tight')

def print_result(pop, its):
    print "Generation "+str(its)+":"
    print str(pop.paths[0].cost)
    print str(pop.bestVertices())
    print ""
    
import graph.plot as gplot
from graph.factory import makeGraph
from graph.genetic import generatePopulation

source = sys.argv[1]
import re
fname = re.sub(r'\.[^\.]+$', "", source)

g = makeGraph(source)
pop = generatePopulation(g,100)

plot(g,pop,fname+"_0")
print_result(pop,0)

its = 0
for iters in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]:
    newIters = iters - its
    its = iters
    for i in range(newIters):
        pop = pop.nextGeneration()
    
    print_result(pop, its)
    plot(g,pop,fname+"_"+str(its))