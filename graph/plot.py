def plotVertices(plot, graph, text=False):
    xs, ys = zip(*graph.vertices)
    plot.scatter(xs, ys, 1)
    if text:
        [plot.annotate(i, (xs[i], ys[i])) for i in range(0,len(xs))]
    return plot

def plotPath(plot, graph, path):
    for v1, v2 in zip(path[:-1], path[1:]):
        x1, y1 = graph.vertices[v1]
        x2, y2 = graph.vertices[v2]
        plot.plot([x1,x2],[y1,y2],'k-')
    return plot