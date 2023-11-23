from typing import Tuple, Optional, Set, FrozenSet
from graph import Graph
from priority_queue import PriorityQueue

def prims_mst (graph: Graph, start_vertex: Optional[str] = None) -> Tuple[Set[FrozenSet[str]], float]:
    """
    Compute the minimum spanning tree using Prim's algorithm.

    Parameters:
        start_vertex (Optional[str]): The starting vertex. If None, the first vertex in the vertices list is used.

    Returns:
        Tuple[Set[FrozenSet[str]], float]: A tuple containing a set of frozensets representing the edges in the MST and the total weight of the MST.

    Time complexity: O(V log V + E) where V is the number of vertices and E is the number of edges (if fibonacci heap is used).
    Space complexity: O(V + E) where V is the number of vertices and E is the number of edges.

    Note: This implementation uses a binary heap instead of a fibonacci heap, so the time complexity is O((V + E) logV).

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 10), ('B', 'C', 1), ('C', 'D', 2), ('D', 'A', 5)], True)
    >>> mst, weight = prims_mst(graph)
    >>> mst
    {frozenset({'C', 'B'}), frozenset({'D', 'C'}), frozenset({'A', 'D'})}
    >>> weight
    8
    """
    if not graph.undirected:
        raise ValueError('Graph must be undirected')

    num_vertices = len(graph.vertices())

    if num_vertices == 0:
        return set(), 0.0

    mst_edges = set()
    total_weight = 0.0
    connected = set()

    # Select the start vertex
    start_vertex = start_vertex or graph.vertices()[0]
    connected.add(start_vertex)

    # Initialize the priority queue
    pq = PriorityQueue(lambda x, y: x[0] < y[0])
    for neighbor, weight in graph.neighbors(start_vertex):
        pq.insert((weight, start_vertex, neighbor))

    while not pq.is_empty() and len(connected) < num_vertices:
        weight, v1, v2 = pq.extract_min()
        if v2 not in connected:
            connected.add(v2)
            mst_edges.add(frozenset({v1, v2}))
            total_weight += weight

            for neighbor, w in graph.neighbors(v2):
                if neighbor not in connected:
                    pq.insert((w, v2, neighbor))

    return mst_edges, total_weight