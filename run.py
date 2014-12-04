#!/usr/bin/env python

import sys, math

from graph.cartesian_graph import CartesianGraph
import graph.plot as gplot
from graph.factory import makeGraph

source = sys.argv[1]
import re
fname = re.sub(r'\.[^\.]+$', "", source)


import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

g = makeGraph(source)

mult = 2**math.floor( math.log10( len(g.vertices) ) )
fig = plt.figure(1, figsize=(mult, mult))

[i.set_linewidth(0.1) for i in plt.gca().spines.itervalues()]

gplot.plotVertices(plt, g)
gplot.plotPath(plt,g,[1,0,4,2,3,1])

plt.xlim(0,plt.xlim()[1]/1.2)
plt.ylim(0,plt.ylim()[1]/1.2)

fig.savefig(fname+".png", bbox_inches='tight')