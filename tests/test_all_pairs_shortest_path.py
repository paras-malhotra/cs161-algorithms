import pytest
from graph import Graph
from floyd_warshall import floyd_warshall_apsp
from breadth_first_search import bfs_apsp
from dijkstra import dijkstra_apsp
from dag_shortest_path import dag_apsp
from johnson import johnson_apsp

unweighted_apsp_algorithms = [floyd_warshall_apsp, johnson_apsp, bfs_apsp, dijkstra_apsp]
positive_weight_algorithms = [floyd_warshall_apsp, johnson_apsp, dijkstra_apsp]
dag_algorithms = [floyd_warshall_apsp, johnson_apsp, dag_apsp]
negative_weight_algorithms = [floyd_warshall_apsp, johnson_apsp]

unweighted_examples = [
    # Simple unweighted graph
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')], {'A': {'A': 0, 'B': 1, 'C': 2, 'D': 1}, 'B': {'B': 0, 'C': 1, 'D': 2, 'A': float('inf')}, 'C': {'C': 0, 'D': 1, 'A': float('inf'), 'B': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
    # Unweighted graph with unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C')], {'A': {'A': 0, 'B': 1, 'C': 2, 'D': float('inf')}, 'B': {'B': 0, 'C': 1, 'D': float('inf'), 'A': float('inf')}, 'C': {'C': 0, 'A': float('inf'), 'B': float('inf'), 'D': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
]

positive_weight_acyclic_examples = [
    # Basic functionality
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)], {'A': {'A': 0, 'B': 1, 'C': 3, 'D': 6}, 'B': {'B': 0, 'C': 2, 'D': 5, 'A': float('inf')}, 'C': {'C': 0, 'D': 3, 'A': float('inf'), 'B': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
    # Complete graph
    (['A', 'B', 'C', 'D'], [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 5), ('B', 'C', 2), ('B', 'D', 6), ('C', 'D', 3)], {'A': {'A': 0, 'B': 4, 'C': 1, 'D': 4}, 'B': {'A': float('inf'), 'B': 0, 'C': 2, 'D': 5}, 'C': {'A': float('inf'), 'B': float('inf'), 'C': 0, 'D': 3}, 'D': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0}}),
    # Star graph
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B', 3), ('A', 'C', 2), ('A', 'D', 4), ('A', 'E', 5)], {'A': {'A': 0, 'B': 3, 'C': 2, 'D': 4, 'E': 5}, 'B': {'A': float('inf'), 'B': 0, 'C': float('inf'), 'D': float('inf'), 'E': float('inf')}, 'C': {'A': float('inf'), 'B': float('inf'), 'C': 0, 'D': float('inf'), 'E': float('inf')}, 'D': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0, 'E': float('inf')}, 'E': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0}}),
    # Unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2)], {'A': {'A': 0, 'B': 1, 'C': 3, 'D': float('inf')}, 'B': {'B': 0, 'C': 2, 'D': float('inf'), 'A': float('inf')}, 'C': {'C': 0, 'A': float('inf'), 'B': float('inf'), 'D': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
]

positive_weight_cyclic_examples = [
    # Positive weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('D', 'A', 10)], {'A': {'A': 0, 'B': 1, 'C': 3, 'D': 6}, 'B': {'B': 0, 'C': 2, 'D': 5, 'A': float('inf')}, 'C': {'C': 0, 'D': 3, 'A': float('inf'), 'B': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
]

negative_weight_acyclic_examples = [
    # Negative-weight edges
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2)], {'A': {'A': 0, 'B': -1, 'C': -3}, 'B': {'B': 0, 'C': -2, 'A': float('inf')}, 'C': {'C': 0, 'A': float('inf'), 'B': float('inf')}}),
]

negative_weight_positive_cycle_examples = [
    # Negative weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'D', -3), ('D', 'A', 10)], {'A': {'A': 0, 'B': -1, 'C': -3, 'D': -6}, 'B': {'B': 0, 'C': -2, 'D': -5, 'A': 5}, 'C': {'C': 0, 'D': -3, 'A': 7, 'B': 6}, 'D': {'D': 0, 'A': 10, 'B': 9, 'C': 7}}),
]

negative_weight_negative_cycle_examples = [
    # Negative-weight cycle
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'A', -3)]),
    # Another negative-weight cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', -5), ('D', 'A', -4)]),
    # Add more cases with negative cycles
]

@pytest.mark.parametrize("algorithm", unweighted_apsp_algorithms)
@pytest.mark.parametrize("vertices, edges, expected_dist", unweighted_examples)
def test_apsp_unweighted_graphs(algorithm, vertices, edges, expected_dist):
    graph = Graph(vertices, edges)
    dist = algorithm(graph)
    assert dist == expected_dist

@pytest.mark.parametrize("algorithm", positive_weight_algorithms)
@pytest.mark.parametrize("vertices, edges, expected_dist", positive_weight_acyclic_examples)
def test_positive_weight_apsp(algorithm, vertices, edges, expected_dist):
    graph = Graph(vertices, edges)
    dist = algorithm(graph)
    assert dist == expected_dist

@pytest.mark.parametrize("algorithm", dag_algorithms)
@pytest.mark.parametrize("vertices, edges, expected_dist", positive_weight_acyclic_examples + negative_weight_acyclic_examples)
def test_dag_apsp(algorithm, vertices, edges, expected_dist):
    graph = Graph(vertices, edges)
    dist = algorithm(graph)
    assert dist == expected_dist

@pytest.mark.parametrize("algorithm", negative_weight_algorithms)
@pytest.mark.parametrize("vertices, edges, expected_dist", negative_weight_positive_cycle_examples)
def test_negative_weight_apsp(algorithm, vertices, edges, expected_dist):
    graph = Graph(vertices, edges)
    dist = algorithm(graph)
    assert dist == expected_dist

@pytest.mark.parametrize("algorithm", negative_weight_algorithms)
@pytest.mark.parametrize("vertices, edges", negative_weight_negative_cycle_examples)
def test_apsp_negative_cycle(algorithm, vertices, edges):
    graph = Graph(vertices, edges)
    with pytest.raises(ValueError, match='Graph contains a negative-weight cycle'):
        algorithm(graph)
