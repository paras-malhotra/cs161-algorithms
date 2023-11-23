from typing import Tuple, Optional, Set, FrozenSet
from graph import Graph
from priority_queue import PriorityQueue
from union_find import UnionFind
from quick_sort import quick_sort

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

def kruskals_mst(graph: Graph) -> Tuple[Set[FrozenSet[str]], float]:
    """
    Compute the minimum spanning tree using Kruskal's algorithm.

    Parameters:
        graph (Graph): The graph on which to compute the MST.

    Returns:
        Tuple[Set[FrozenSet[str]], float]: A tuple containing a set of frozensets representing the edges in the MST and the total weight of the MST.

    Time complexity: O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.
    Space complexity: O(V + E) where V is the number of vertices and E is the number of edges.

    Example:
    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 10), ('B', 'C', 1), ('C', 'D', 2), ('D', 'A', 5)], True)
    >>> mst, weight = kruskals_mst(graph)
    >>> mst
    {frozenset({'C', 'B'}), frozenset({'D', 'C'}), frozenset({'A', 'D'})}
    >>> weight
    8
    """
    if not graph.undirected:
        raise ValueError('Graph must be undirected')

    # Initialize Union-Find data structure
    uf = UnionFind()
    for vertex in graph.vertices():
        # All vertices are initially in their own set
        uf.make_set(vertex)

    # Sort edges by weight
    edges = quick_sort(graph.edges(), comparator=lambda e1, e2: e1[2] < e2[2])

    mst_edges = set()
    total_weight = 0.0
    num_vertices = len(graph.vertices())

    for v1, v2, weight in edges:
        if not uf.connected(v1, v2):
            uf.union(v1, v2)
            mst_edges.add(frozenset({v1, v2}))
            total_weight += weight
            if len(mst_edges) == num_vertices - 1:
                # Early exit if we have found all edges as MST has exactly V - 1 edges
                break

    return mst_edges, total_weight
