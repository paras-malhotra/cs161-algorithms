import pytest
from graph import Graph
from bellman_ford import bellman_ford_sssp
from breadth_first_search import bfs_sssp
from dijkstra import dijkstra_sssp

unweighted_algorithms = [bellman_ford_sssp, bfs_sssp, dijkstra_sssp]
positive_weight_algorithms = [bellman_ford_sssp, dijkstra_sssp]
negative_weight_sssp_algorithms = [bellman_ford_sssp]

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

@pytest.mark.parametrize("algorithm", positive_weight_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", [
    # Positive weights, no cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('A', 'D', 10)], 'A', {'A': 0, 'B': 1, 'C': 3, 'D': 6}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}),
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 3), ('C', 'D', 1), ('D', 'E', 4)], 'A', {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 7}, {'A': None, 'B': 'A', 'C': 'A', 'D': 'C', 'E': 'D'}),
    # Star graph
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B', 1), ('A', 'C', 3), ('A', 'D', 5), ('A', 'E', 7)], 'A', {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'E': 7}, {'A': None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': 'A'}),
    # Binary Tree Graph
    (['A', 'B', 'C', 'D', 'E', 'F', 'G'], [('A', 'B', 2), ('A', 'C', 3), ('B', 'D', 4), ('B', 'E', 5), ('C', 'F', 6), ('C', 'G', 7)], 'A', {'A': 0, 'B': 2, 'C': 3, 'D': 6, 'E': 7, 'F': 9, 'G': 10}, {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'C', 'G': 'C'}),
    # Positive weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('D', 'A', 10)], 'A', {'A': 0, 'B': 1, 'C': 3, 'D': 6}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}),
    # Unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2)], 'A', {'A': 0, 'B': 1, 'C': 3, 'D': float('inf')}, {'A': None, 'B': 'A', 'C': 'B', 'D': None}),
    # Single vertex
    (['A'], [], 'A', {'A': 0}, {'A': None}),
])
def test_sssp_positive_weighted_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", negative_weight_sssp_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", [
    # Negative weights
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2), ('A', 'C', -2)], 'A', {'A': 0, 'B': -1, 'C': -3}, {'A': None, 'B': 'A', 'C': 'B'}),
    # Negative weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'D', -3), ('D', 'A', 10)], 'A', {'A': 0, 'B': -1, 'C': -3, 'D': -6}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}),
])
def test_sssp_negative_weighted_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", negative_weight_sssp_algorithms)
@pytest.mark.parametrize("vertices, edges", [
    # Negative-weight cycles
    (['A', 'B', 'C'], [('A', 'B', 1), ('B', 'C', -2), ('C', 'A', -1)]),
    (['A', 'B', 'C', 'D'], [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', -5), ('D', 'A', -4)]),
])
def test_sssp_negative_cycle(algorithm, vertices, edges):
    graph = Graph(vertices, edges)
    with pytest.raises(ValueError, match='Graph contains a negative-weight cycle'):
        algorithm(graph, vertices[0])
