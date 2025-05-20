import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from code.shortestpath import dijkstra, Graph  # Graph'ı da alıyoruz

def test_dijkstra():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    distances, _ = dijkstra(g, 'A')
    assert distances['D'] == 4
    assert distances['C'] == 3
