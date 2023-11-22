from typing import Dict
from graph import Graph
from bellman_ford import bellman_ford_sssp
from dijkstra import dijkstra_sssp

def johnson_apsp(graph: Graph) -> Dict[str, Dict[str, float]]:
    """
    Johnson's algorithm for all-pairs shortest paths. Can be used to detect negative-weight cycles.

    Parameters:
        graph (Graph): The graph to traverse.

    Returns:
        Dict[str, Dict[str, float]]: The shortest distances between all pairs of vertices.

    Time complexity: O(V^2 logV + VE) where V is the number of vertices and E is the number of edges (if fibonacci heap is used).
    Space complexity: O(V^2) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)])
    >>> dist = johnson_apsp(graph)
    >>> dist['A']['D']
    6
    """
    # Add a new vertex and connect it to all other vertices with zero-weight edges
    graph.add_vertex('S')
    for vertex in graph.vertices():
        graph.add_edge('S', vertex, 0)

    # Run Bellman-Ford algorithm to find the shortest distances from the new vertex to all other vertices
    dist_from_new_vertex, _ = bellman_ford_sssp(graph, 'S')

    # Remove the new vertex and its edges
    graph.remove_vertex('S')

    # Recompute the weights of all edges
    for u, v, w in graph.edges():
        graph.remove_edge(u, v)
        graph.add_edge(u, v, w + dist_from_new_vertex[u] - dist_from_new_vertex[v])

    # Run Dijkstra's algorithm for all vertices
    all_dist = {}
    for vertex in graph.vertices():
        dist, _ = dijkstra_sssp(graph, vertex)
        all_dist[vertex] = dist

    # Restore the original weights of all edges
    for u, v, w in graph.edges():
        graph.remove_edge(u, v)
        graph.add_edge(u, v, w - dist_from_new_vertex[u] + dist_from_new_vertex[v])

    # Fix the distances
    for u in graph.vertices():
        for v in graph.vertices():
            all_dist[u][v] = all_dist[u][v] - dist_from_new_vertex[u] + dist_from_new_vertex[v]

    return all_dist