#!/usr/bin/env python2

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
    
    fig.savefig(fname+".png", bbox_inches='tight')

def print_result(path, cost, msg):
    cientcost = "%e" % cost
    sys.stderr.write("[INFO] "+msg+": "+cientcost+"\n")
    print msg+" :"
    print str(cost)
    print str(path)
    print ""

def print_genetic_result(pop, its):
    print_result(pop.bestVertices(), pop.bestPath().cost, "Generation #"+str(its))

import graph.plot as gplot
from graph.factory import makeGraph
from graph.genetic import generatePopulation

def run():
    source = sys.argv[1]
    import re
    fname = re.sub(r'\.[^\.]+$', "", source)
    sys.stderr.write("[INFO] Loading graph...\n")
    g = makeGraph(source)

    run_genetic(g,fname)

from graph.genetic import generateNeighborsPath
def run_two_op(g,fname):
    sys.stderr.write("[INFO] Generating nearestNeighbors\n")
    firstPath = generateNeighborsPath(G)


def run_genetic(g,fname):
    sys.stderr.write("[INFO] Generating generation #0\n")
    pop = generatePopulation(g,100)

    plot(g,pop,fname+"_0")
    print_genetic_result(pop,0)

    its = 0
    for iters in [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]:
        newIters = iters - its
        its = iters
        for i in range(newIters):
            pop = pop.nextGeneration()
        
        print_genetic_result(pop, its)
        plot(g,pop,fname+"_"+str(its))

run()
