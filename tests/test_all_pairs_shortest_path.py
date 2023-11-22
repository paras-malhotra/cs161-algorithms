import pytest
from graph import Graph
from floyd_warshall import floyd_warshall_apsp
from breadth_first_search import bfs_apsp

apsp_algorithms = [floyd_warshall_apsp]
unweighted_apsp_algorithms = [floyd_warshall_apsp, bfs_apsp]

@pytest.mark.parametrize("algorithm", unweighted_apsp_algorithms)
@pytest.mark.parametrize("vertices, edges, expected_dist", [
    # Simple unweighted graph
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')], {'A': {'A': 0, 'B': 1, 'C': 2, 'D': 1}, 'B': {'B': 0, 'C': 1, 'D': 2, 'A': float('inf')}, 'C': {'C': 0, 'D': 1, 'A': float('inf'), 'B': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
    # Unweighted graph with unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C')], {'A': {'A': 0, 'B': 1, 'C': 2, 'D': float('inf')}, 'B': {'B': 0, 'C': 1, 'D': float('inf'), 'A': float('inf')}, 'C': {'C': 0, 'A': float('inf'), 'B': float('inf'), 'D': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
])
def test_apsp_unweighted_graphs(algorithm, vertices, edges, expected_dist):
    graph = Graph(vertices, edges)
    dist = algorithm(graph)
    assert dist == expected_dist

@pytest.mark.parametrize("algorithm", apsp_algorithms)
@pytest.mark.parametrize("vertices, edges, expected_dist", [
    # Basic functionality
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)], {'A': {'A': 0, 'B': 1, 'C': 3, 'D': 6}, 'B': {'B': 0, 'C': 2, 'D': 5, 'A': float('inf')}, 'C': {'C': 0, 'D': 3, 'A': float('inf'), 'B': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
    # Negative weights with positive cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'D', -3), ('D', 'A', 10)], {'A': {'A': 0, 'B': -1, 'C': -3, 'D': -6}, 'B': {'B': 0, 'C': -2, 'D': -5, 'A': 5}, 'C': {'C': 0, 'D': -3, 'A': 7, 'B': 6}, 'D': {'D': 0, 'A': 10, 'B': 9, 'C': 7}}),
    # Unreachable vertex
    (['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2)], {'A': {'A': 0, 'B': 1, 'C': 3, 'D': float('inf')}, 'B': {'B': 0, 'C': 2, 'D': float('inf'), 'A': float('inf')}, 'C': {'C': 0, 'A': float('inf'), 'B': float('inf'), 'D': float('inf')}, 'D': {'D': 0, 'A': float('inf'), 'B': float('inf'), 'C': float('inf')}}),
    # Negative-weight edges
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2)], {'A': {'A': 0, 'B': -1, 'C': -3}, 'B': {'B': 0, 'C': -2, 'A': float('inf')}, 'C': {'C': 0, 'A': float('inf'), 'B': float('inf')}}),
])
def test_apsp(algorithm, vertices, edges, expected_dist):
    graph = Graph(vertices, edges)
    dist = algorithm(graph)
    assert dist == expected_dist

@pytest.mark.parametrize("algorithm", apsp_algorithms)
@pytest.mark.parametrize("vertices, edges", [
    # Negative-weight cycle
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'A', -3)]),
    # Another negative-weight cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', -5), ('D', 'A', -4)]),
    # Add more cases with negative cycles
])
def test_apsp_negative_cycle(algorithm, vertices, edges):
    graph = Graph(vertices, edges)
    with pytest.raises(ValueError, match='Graph contains a negative-weight cycle'):
        algorithm(graph)
