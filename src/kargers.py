from graph import Graph
from union_find import UnionFind
import random
from typing import Optional
import math

def kargers_min_cut_iteration_unweighted(graph: Graph) -> int:
    """
    Perform one iteration of the Karger's algorithm to find the minimum cut of the graph using random contraction. Only works for undirected and unweighted graphs.

    Parameters:
        graph (Graph): The graph.

    Returns:
        int: The estimated minimum cut of the graph after one iteration. This is not guaranteed to be the actual minimum cut.

    Time complexity: O(E * α(V)), where α(V) is the inverse Ackermann function, effectively constant.
    Space complexity: O(V) where V is the number of vertices.
    """
    # Create a Union-Find structure
    uf = UnionFind()

    # Add all vertices to the Union-Find structure
    for v in graph.vertices():
        uf.make_set(v)

    # Keep track of the number of vertices
    num_vertices = len(graph.vertices())

    # Keep contracting the graph until only two vertices remain
    while num_vertices > 2:
        # Pick a random edge
        v1, v2, _ = random.choice(graph.edges())

        # If the two vertices are not in the same set, contract the edge
        if uf.find(v1) != uf.find(v2):
            # Merge the two vertices
            uf.union(v1, v2)

            # Decrement the number of vertices
            num_vertices -= 1

    # Count the number of edges between the two sets
    min_cut = 0
    for v1, v2, _ in graph.edges():
        if uf.find(v1) != uf.find(v2):
            min_cut += 1

    return min_cut

def kargers_min_cut_unweighted(graph: Graph, num_iterations: Optional[int] = None) -> int:
    """
    Find the minimum cut of the graph using Karger's algorithm. Only works for undirected and unweighted graphs.

    Parameters:
        graph (Graph): The graph.
        num_iterations (int): The number of iterations to perform. Defaults to n^2 * log(n), where n is the number of vertices in the graph.

    Returns:
        int: The minimum cut of the graph. This is not guaranteed to be the actual minimum cut but the probability of failure is very low if the number of iterations is high enough.

    Time complexity: O(num_iterations * E * α(V)), where α(V) is the inverse Ackermann function, effectively constant.
    Space complexity: O(V) where V is the number of vertices.
    """
    # Keep track of the minimum cut
    min_cut = float("inf")

    n = len(graph.vertices())
    if num_iterations is None:
        num_iterations = n ** 2 * int(math.log(n))

    for _ in range(num_iterations):
        # Perform one iteration of the algorithm
        min_cut = min(min_cut, kargers_min_cut_iteration_unweighted(graph))

    return min_cut