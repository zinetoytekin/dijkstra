import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from code.shortestpath import dijkstra  
 

def test_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    result = dijkstra(graph, 'A')
    assert result['D'] == 4
    assert result['C'] == 3
