from typing import Dict, Tuple
from graph import Graph
from depth_first_search import topological_sort

def dag_sssp(graph: Graph, source: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Single-source shortest paths (SSSP) for directed acyclic graphs (DAGs).

    Parameters:
        graph (Graph): The graph to traverse.
        source (str): The source vertex.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)])
    >>> dist, pred = dag_sssp(graph, 'A')
    >>> dist['D']
    6
    >>> pred['D']
    'C'
    """
    # Initialize distance and predecessor dictionaries
    dist = {v: float('inf') for v in graph.vertices()}
    pred = {v: None for v in graph.vertices()}

    # Set the source distance to 0
    dist[source] = 0

    # Topologically sort the vertices
    vertices = topological_sort(graph)

    # Loop through the vertices in topological order
    for vertex in vertices:
        # Loop through the neighbors of the current vertex
        for neighbor, weight in graph.neighbors(vertex):
            # Relax the distance to the neighbor
            new_dist = dist[vertex] + weight

            # Update the distance and predecessor if the new distance is less than the current distance
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                pred[neighbor] = vertex

    return dist, pred

def dag_apsp(graph: Graph) -> Dict[str, Dict[str, float]]:
    """
    All-pairs shortest paths (APSP) for directed acyclic graphs (DAGs).

    Parameters:
        graph (Graph): The graph to traverse.

    Returns:
        Dict[str, Dict[str, float]]: The shortest distances between all pairs of vertices.

    Time complexity: O(V * (V + E)) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V^2) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)])
    >>> dist = dag_apsp(graph)
    >>> dist['A']['D']
    6
    """
    dist = {}
    for vertex in graph.vertices():
        dist[vertex] = dag_sssp(graph, vertex)[0]
    return dist