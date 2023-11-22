from typing import Dict, Callable, Optional, Tuple
from graph import Graph
from linked_queue import Queue

def breadth_first_search(graph: Graph, start: Optional[str], callback: Optional[Callable[[str, Optional[str]], None]]) -> Dict[str, str]:
    """
    Breadth-first search (BFS) for traversing or searching graph data structures.

    Arguments:
        graph (Graph): Graph to search.
        start (Optional[str]): The starting vertex, or None to search the entire graph.
        callback (Optional[Callable[[str, Optional[str]], None]]): Optional callback function for each visited vertex.

    Returns:
        Dict[str, str]: A dictionary containing the parent of each vertex in the graph.

    Time complexity: O(V + E)
    """
    visited = {vertex: False for vertex in graph.vertices()}
    parents = {vertex: None for vertex in graph.vertices()}

    def bfs_from_vertex(vertex: str):
        queue = Queue()
        queue.enqueue(vertex)

        while not queue.is_empty():
            current = queue.dequeue()
            if not visited[current]:
                visited[current] = True
                if callback:
                    callback(current, parents[current])
                for neighbor, _ in graph.neighbors(current):
                    if not visited[neighbor]:
                        queue.enqueue(neighbor)
                        parents[neighbor] = current

    if start is None:
        for vertex in graph.vertices():
            if not visited[vertex]:
                bfs_from_vertex(vertex)
    else:
        bfs_from_vertex(start)

    return parents

def bfs_sssp(graph: Graph, source: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Breadth-first search (BFS) algorithm for single-source shortest paths.

    Parameters:
        graph (Graph): The graph to traverse.
        source (str): The source vertex.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D')])
    >>> dist, pred = bfs_sssp(graph, 'A')
    >>> dist['D']
    3
    >>> pred['D']
    'C'
    """
    dist = {v: float('inf') for v in graph.vertices()}
    dist[source] = 0
    def record_distance(vertex: str, parent: Optional[str]) -> None:
        if parent is not None:
            dist[vertex] = dist[parent] + 1
    pred = breadth_first_search(graph, source, record_distance)
    return dist, pred

def bfs_apsp(graph: Graph) -> Dict[str, Dict[str, int]]:
    """
    Breadth-first search (BFS) algorithm for all-pairs shortest paths.

    Parameters:
        graph (Graph): The graph to traverse.

    Returns:
        Dict[str, Dict[str, int]]: The shortest distances between all pairs of vertices.

    Time complexity: O(V * (V + E)) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V^2) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D')])
    >>> dist = bfs_apsp(graph)
    >>> dist['A']['D']
    3
    """
    dist = {}
    for vertex in graph.vertices():
        dist[vertex], _ = bfs_sssp(graph, vertex)
    return dist

def check_bipartite(graph: Graph) -> bool:
    """
    A graph is bipartite if its vertices can be divided into two independent sets (or, equivalently, two color classes)
    such that every edge connects a vertex in one set with a vertex in the other set. The graph is assumed to be connected.

    Parameters:
        graph (Graph): The graph to check.

    Returns:
        bool: True if the graph is bipartite, False otherwise.

    Time complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D')])
    >>> check_bipartite(graph)
    True
    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')])
    >>> check_bipartite(graph)
    True
    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C')])
    >>> check_bipartite(graph)
    False
    """
    # Initialize color dictionary
    colors = {vertex: None for vertex in graph.vertices()}

    def color(vertex: str, parent: Optional[str]) -> None:
        # Color the vertex the opposite color of its parent
        colors[vertex] = 0 if (parent is None or colors[parent] == 1) else 1

    breadth_first_search(graph, None, color)

    # Check for an edge between two vertices of the same color
    for u, v, _ in graph.edges():
        if colors[u] == colors[v]:
            return False

    return True