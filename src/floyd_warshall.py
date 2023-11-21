from graph import Graph

def floyd_warshall_apsp(graph: Graph) -> dict[str, dict[str, float]]:
    """
    Floyd-Warshall algorithm for all-pairs shortest paths. This algorithm can detect negative-weight cycles.

    Parameters:
        graph (Graph): The graph to traverse.

    Returns:
        dict[str, dict[str, float]]: The shortest distances between all pairs of vertices.

    Time complexity: O(V^3) where V is the number of vertices.
    Space complexity: O(V^2) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)])
    >>> dist = floyd_warshall_apsp(graph)
    >>> dist['A']['D']
    6
    """
    # Initialize distance dictionary
    dist = {u: {v: float('inf') for v in graph.vertices()} for u in graph.vertices()}

    # Set the distance to self to 0
    for v in graph.vertices():
        dist[v][v] = 0

    # Set the distance to neighbors
    for u, v, w in graph.edges():
        dist[u][v] = w

    # Find the shortest path between every pair of vertices
    for k in graph.vertices():
        for u in graph.vertices():
            for v in graph.vertices():
                # At every iteration, the shortest path is relaxed by considering vertex k as an intermediate vertex
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    # Check for negative-weight cycles
    for u in graph.vertices():
        # If the distance from a vertex to itself is negative, then there is a negative-weight cycle
        if dist[u][u] < 0:
            raise ValueError('Graph contains a negative-weight cycle')

    return dist