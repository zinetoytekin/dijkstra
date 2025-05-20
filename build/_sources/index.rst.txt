Shortest Path Finder Documentation
==================================

A Python package implementing Dijkstra's algorithm for finding shortest paths in graphs.

Key Features
------------
- **Flexible graphs**: Supports both directed and undirected graphs
- **Positive weights**: Works with zero or positive edge weights
- **Dynamic structure**: Add nodes and edges at runtime
- **Optimal performance**: Uses Python's heapq for efficiency
- **Detailed output**: Returns both path and total distance

Quick Start
-----------
Basic usage example:

.. code-block:: python

   from dijkstra_shortest_path import Graph, shortest_path

   # Create a new graph
   network = Graph()
   
   # Add nodes
   network.add_node('A')
   network.add_node('B')
   network.add_node('C')
   
   # Add edges (with distances)
   network.add_edge('A', 'B', 5)
   network.add_edge('B', 'C', 3)
   network.add_edge('A', 'C', 9)
   
   # Calculate shortest path
   path, distance = shortest_path(network, 'A', 'C')
   
   print(f"Optimal path: {' → '.join(path)}")
   print(f"Total distance: {distance}")

API Reference
-------------
.. toctree::
   :maxdepth: 2
   :caption: API Documentation:
   
   api/graph_class
   api/dijkstra_function
   api/shortest_path_function

Additional Resources
--------------------
- `GitHub Repository <https://github.com/zinetoytekin/dijkstra.git>`_
.. note::
   This library is suitable for both academic and commercial use.
   Please report any issues on GitHub.
