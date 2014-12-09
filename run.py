#!/usr/bin/env python2

import sys, math

def plot(g, path, fname):
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt
    plt.close('all')
    
    mult = 2**math.floor( math.log10( len(g.vertices) ) )
    fig = plt.figure(1, figsize=(2*mult, 2*mult))
    
    [i.set_linewidth(0.1) for i in plt.gca().spines.itervalues()]
    
    gplot.plotVertices(plt, g)
    gplot.plotPath(plt,g,path)
    
    fig.savefig(fname+".png", bbox_inches='tight')

def plot_genetic(g, population, fname):
    plot(g, population.bestVertices(), fname)

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

    runners = {
        "genetic": run_genetic,
        "2opt": run_nn_two_opt,
        "amorim": run_amorim,
        "amorim2opt": run_amorim_two_opt
    }
    runner = "genetic"
    if len(sys.argv) >= 3:
        runner = sys.argv[2]

    runners[runner](g,fname)

from graph.amorim import amorim
def run_amorim(g,fname):
    sys.stderr.write("[INFO] Running Amorim's Algorithm\n")
    path = amorim(g)
    print_result(path, g.pathCost(path), "Amorim Algo's")
    plot(g, path, fname+"_amorim")
    return path

def run_amorim_two_opt(g,fname):
    path = run_amorim(g,fname)
    run_two_opt(g,fname+"_amorim",path)

from graph.generators import generateNeighborsPath
from graph import two_opt
def run_two_opt(g,fname,path):
    curr_iter = 0

    path = path
    for nppath in two_opt.improvePath(g, path):
        path = nppath
        curr_iter = curr_iter + 1
        if math.log10(curr_iter) % 1 == 0:
            path = list(path)
            print_result(path, g.pathCost(path), "Iter #"+str(curr_iter))
            plot(g, path, fname+"_2opt_"+str(curr_iter))
    path = list(path)
    print_result(path, g.pathCost(path), "Final 2opt")
    plot(g,path,fname+"_2opt")

def run_nn_two_opt(g,fname):
    sys.stderr.write("[INFO] Generating nearestNeighbors\n")
    path = generateNeighborsPath(g,None,1)

    print_result(path, g.pathCost(path), "Nearest Neighbors Path")
    plot(g, path, fname+"_nn")

    run_two_opt(g,fname,path)

def run_genetic(g,fname):
    sys.stderr.write("[INFO] Generating generation #0\n")
    pop = generatePopulation(g,100)

    plot_genetic(g,pop,fname+"_0")
    print_genetic_result(pop,0)

    its = 0
    for iters in [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]:
        newIters = iters - its
        its = iters
        for i in range(newIters):
            pop = pop.nextGeneration()
        
        print_genetic_result(pop, its)
        plot_genetic(g,pop,fname+"_"+str(its))

run()
