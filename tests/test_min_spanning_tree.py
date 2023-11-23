import pytest
from minimum_spanning_tree import prims_mst
from graph import Graph

@pytest.mark.parametrize("algorithm", [prims_mst])
@pytest.mark.parametrize("vertices, edges, expected_mst, expected_weight", [
    # Simple graph
    (['A', 'B', 'C'], [('A', 'B', 1), ('B', 'C', 2)], {frozenset({'A', 'B'}), frozenset({'B', 'C'})}, 3),

    # Graph with multiple connected components
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B', 1), ('B', 'C', 3), ('D', 'E', 2)], {frozenset({'A', 'B'}), frozenset({'B', 'C'})}, 4),

    # Graph with heavier and lighter edges
    (['A', 'B', 'C', 'D'], [('A', 'B', 10), ('B', 'C', 1), ('C', 'D', 2), ('D', 'A', 5)], {frozenset({'B', 'C'}), frozenset({'C', 'D'}), frozenset({'D', 'A'})}, 8),

    # Graph with cycles
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('D', 'A', 4), ('B', 'D', 5)], {frozenset({'A', 'B'}), frozenset({'B', 'C'}), frozenset({'C', 'D'})}, 6),

    # Dense graph
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 3), ('B', 'C', 4), ('B', 'D', 5), ('C', 'D', 6)], {frozenset({'A', 'B'}), frozenset({'A', 'C'}), frozenset({'A', 'D'})}, 6),

    # Graph with multiple paths and varying weights
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B', 3), ('A', 'C', 1), ('B', 'C', 7), ('B', 'D', 5), ('C', 'D', 8), ('D', 'E', 2)], {frozenset({'A', 'C'}), frozenset({'A', 'B'}), frozenset({'B', 'D'}), frozenset({'D', 'E'})}, 11),

    # Large graph with various edge weights
    (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], [('A', 'B', 8), ('B', 'C', 10), ('C', 'D', 3), ('D', 'E', 4), ('E', 'F', 12), ('F', 'G', 7), ('G', 'H', 2), ('H', 'A', 5), ('B', 'E', 6), ('C', 'F', 1), ('D', 'G', 9)], {frozenset({'C', 'F'}), frozenset({'G', 'H'}), frozenset({'C', 'D'}), frozenset({'D', 'E'}), frozenset({'H', 'A'}), frozenset({'F', 'G'}), frozenset({'E', 'B'})}, 28),

    # Disconnected graph
    (['A', 'B', 'C', 'D'], [('A', 'B', 1)], {frozenset({'A', 'B'})}, 1),
])
def test_mst(algorithm, vertices, edges, expected_mst, expected_weight):
    graph = Graph(vertices, edges, undirected=True)
    mst, weight = algorithm(graph)
    assert mst == expected_mst
    assert weight == expected_weight