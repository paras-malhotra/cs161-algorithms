from graph import Graph

def bellman_ford_sssp(graph: Graph, source: str) -> tuple[dict[str, float], dict[str, str]]:
    """
    Bellman-Ford algorithm for single-source shortest paths. This algorithm does not work with negative-weight cycles.

    Parameters:
        graph (Graph): The graph to traverse.
        source (str): The source vertex.

    Returns:
        tuple[dict[str, float], dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(VE) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)])
    >>> dist, pred = bellman_ford_sssp(graph, 'A')
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

    # Relax the edges repeatedly (V - 1 times). At every iteration, the shortest path with at most i edges is found.
    # i cannot be greater than V - 1 because the shortest path cannot have a cycle (unless it is negative-weight).
    for _ in range(len(graph.vertices()) - 1):
        for u, v, w in graph.edges():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

    # Check for negative-weight cycles
    for u, v, w in graph.edges():
        if dist[u] + w < dist[v]:
            raise ValueError('Graph contains a negative-weight cycle')

    return dist, pred