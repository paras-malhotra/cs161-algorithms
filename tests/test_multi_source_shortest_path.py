import pytest
from graph import Graph
from multi_source_shortest_path import dijkstra_mssp, dag_mssp, bellman_ford_mssp, bfs_mssp

unweighted_algorithms = [bellman_ford_mssp, bfs_mssp, dijkstra_mssp]
positive_weight_algorithms = [bellman_ford_mssp, dijkstra_mssp]
dag_algorithms = [bellman_ford_mssp, dag_mssp]
negative_weight_mssp_algorithms = [bellman_ford_mssp]

unweighted_examples = [
    # Simple unweighted graph
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')], ['A', 'B'], {'A': 0, 'B': 0, 'C': 1, 'D': 1}, {'A': None, 'B': None, 'C': 'B', 'D': 'A'}),
    # Unweighted graph with unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C')], ['A', 'B'], {'A': 0, 'B': 0, 'C': 1, 'D': float('inf')}, {'A': None, 'B': None, 'C': 'B', 'D': None}),
    # Single source
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')], ['A'], {'A': 0, 'B': 1, 'C': 2, 'D': 1}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'A'}),
]

positive_weight_acyclic_examples = [
    # Positive weights, no cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('A', 'D', 10)], ['A', 'B'], {'A': 0, 'B': 0, 'C': 2, 'D': 5}, {'A': None, 'B': None, 'C': 'B', 'D': 'C'}),
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 2), ('C', 'D', 1), ('D', 'E', 4)], ['A', 'B'], {'A': 0, 'B': 0, 'C': 2, 'D': 2, 'E': 6}, {'A': None, 'B': None, 'C': 'A', 'D': 'B', 'E': 'D'}),
    # Star graph
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B', 1), ('A', 'C', 3), ('A', 'D', 5), ('A', 'E', 7)], ['A', 'B'], {'A': 0, 'B': 0, 'C': 3, 'D': 5, 'E': 7}, {'A': None, 'B': None, 'C': 'A', 'D': 'A', 'E': 'A'}),
    # Binary Tree Graph
    (['A', 'B', 'C', 'D', 'E', 'F', 'G'], [('A', 'B', 2), ('A', 'C', 3), ('B', 'D', 4), ('B', 'E', 5), ('C', 'F', 6), ('C', 'G', 7)], ['A', 'B'], {'A': 0, 'B': 0, 'C': 3, 'D': 4, 'E': 5, 'F': 9, 'G': 10}, {'A': None, 'B': None, 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'C', 'G': 'C'}),
    # Unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2)], ['A', 'B'], {'A': 0, 'B': 0, 'C': 2, 'D': float('inf')}, {'A': None, 'B': None, 'C': 'B', 'D': None}),
]

positive_weight_cyclic_examples = [
    # Positive weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('D', 'A', 10)], ['A', 'B'], {'A': 0, 'B': 0, 'C': 2, 'D': 5}, {'A': None, 'B': None, 'C': 'B', 'D': 'C'}),
]

negative_weight_acyclic_examples = [
    # Negative weights
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2), ('A', 'C', -2)], ['A', 'B'], {'A': 0, 'B': -1, 'C': -3}, {'A': None, 'B': 'A', 'C': 'B'}),
]

negative_weight_cyclic_examples = [
    # Negative weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'D', -3), ('D', 'A', 10)], ['A', 'B'], {'A': 0, 'B': -1, 'C': -3, 'D': -6}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}),
]

negative_weight_negative_cycle_examples = [
    # Negative-weight cycles
    (['A', 'B', 'C'], [('A', 'B', 1), ('B', 'C', -2), ('C', 'A', -1)]),
    (['A', 'B', 'C', 'D'], [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', -5), ('D', 'A', -4)]),
]

@pytest.mark.parametrize("algorithm", unweighted_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", unweighted_examples)
def test_mssp_unweighted_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", positive_weight_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", positive_weight_acyclic_examples + positive_weight_cyclic_examples)
def test_mssp_positive_weighted_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", dag_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", positive_weight_acyclic_examples + negative_weight_acyclic_examples)
def test_mssp_dag_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", negative_weight_mssp_algorithms)
@pytest.mark.parametrize("vertices, edges, source, expected_dist, expected_pred", negative_weight_acyclic_examples + negative_weight_cyclic_examples)
def test_mssp_negative_weighted_graphs(algorithm, vertices, edges, source, expected_dist, expected_pred):
    graph = Graph(vertices, edges)
    dist, pred = algorithm(graph, source)
    assert dist == expected_dist
    assert pred == expected_pred

@pytest.mark.parametrize("algorithm", negative_weight_mssp_algorithms)
@pytest.mark.parametrize("vertices, edges", negative_weight_negative_cycle_examples)
def test_sssp_negative_cycle(algorithm, vertices, edges):
    graph = Graph(vertices, edges)
    with pytest.raises(ValueError, match='Graph contains a negative-weight cycle'):
        algorithm(graph, vertices[0])
