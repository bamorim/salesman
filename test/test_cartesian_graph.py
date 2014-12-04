import unittest
from graph.cartesian_graph import CartesianGraph


class TestCartesianGraph(unittest.TestCase):
    def test_some_edges(self):
        graph = CartesianGraph()
        v1 = graph.add( 0 , 0 )
        v2 = graph.add( 3 , 4 )
        _, _, weight = graph.getEdge( v1 , v2 )
        self.assertEqual( 5 , weight )
        
    def test_graph_cost(self):
        graph = CartesianGraph()
        v1 = graph.add( 0 , 0 )
        v2 = graph.add( 0 , 1 )
        v3 = graph.add( 1 , 1 )
        self.assertEqual( 2 , graph.path_cost( [v1, v2, v3] ) )

if __name__ == '__main__':
	unittest.main()