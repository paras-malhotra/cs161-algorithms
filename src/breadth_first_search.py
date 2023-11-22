from typing import Dict, Callable, Optional, Tuple
from graph import Graph
from linked_queue import Queue

def breadth_first_search(graph: Graph, start: str, callback: Optional[Callable[[str, Optional[str]], None]] = None) -> Dict[str, str]:
    """
    Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
    It starts at the tree root (or some arbitrary node of a graph) and explores the neighbor nodes first,
    before moving to the next level neighbors.

    Arguments:
        graph (Graph): Graph to search.
        start (str): Starting vertex.
        callback (Optional[Callable[[str, Optional[str]], None]]): Optional callback function to be called when a vertex is visited.

    Returns:
        Dict[str, str]: A dictionary containing the parent of each vertex in the graph.

    Time complexity: O(V + E)
    """
    visited = {vertex: False for vertex in graph.vertices()}
    parents = {vertex: None for vertex in graph.vertices()}
    queue = Queue()
    queue.enqueue(start)
    while not queue.is_empty():
        vertex = queue.dequeue()
        if not visited[vertex]:
            visited[vertex] = True
            if callback:
                callback(vertex, parents[vertex])
            for neighbor, _ in graph.neighbors(vertex):
                if not visited[neighbor]:
                    queue.enqueue(neighbor)
                    parents[neighbor] = vertex

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