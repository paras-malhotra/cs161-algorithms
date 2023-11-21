import pytest
from graph import Graph
from bellman_ford import bellman_ford_sssp
from bfs import bfs_sssp

sssp_algorithms = [bellman_ford_sssp]
unweighted_algorithms = [bellman_ford_sssp, bfs_sssp]

@pytest.mark.parametrize("algorithm", unweighted_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", [
    # Simple unweighted graph
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')], 'A', {'A': 0, 'B': 1, 'C': 2, 'D': 1}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'A'}),
    # Unweighted graph with unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C')], 'A', {'A': 0, 'B': 1, 'C': 2, 'D': float('inf')}, {'A': None, 'B': 'A', 'C': 'B', 'D': None}),
])
def test_sssp_unweighted_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", sssp_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", [
    # Basic functionality
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('A', 'D', 10)], 'A', {'A': 0, 'B': 1, 'C': 3, 'D': 6}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}),
    # Negative weights
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2), ('A', 'C', -2)], 'A', {'A': 0, 'B': -1, 'C': -3}, {'A': None, 'B': 'A', 'C': 'B'}),
    # Negative weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'D', -3), ('D', 'A', 10)], 'A', {'A': 0, 'B': -1, 'C': -3, 'D': -6}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}),
    # Unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2)], 'A', {'A': 0, 'B': 1, 'C': 3, 'D': float('inf')}, {'A': None, 'B': 'A', 'C': 'B', 'D': None}),
    # Empty graph
    ([], [], 'A', {'A': 0}, {}),
    # Single vertex
    (['A'], [], 'A', {'A': 0}, {'A': None}),
])
def test_sssp_weighted_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", sssp_algorithms)
@pytest.mark.parametrize("vertices, edges", [
    # Negative-weight cycles
    (['A', 'B', 'C'], [('A', 'B', 1), ('B', 'C', -2), ('C', 'A', -1)]),
    (['A', 'B', 'C', 'D'], [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', -5), ('D', 'A', -4)]),
])
def test_sssp_negative_cycle(algorithm, vertices, edges):
    graph = Graph(vertices, edges)
    with pytest.raises(ValueError, match='Graph contains a negative-weight cycle'):
        algorithm(graph, vertices[0])
