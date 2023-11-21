import pytest
from graph import Graph
from floyd_warshall import floyd_warshall_apsp

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
def test_floyd_warshall(vertices, edges, expected_dist):
    graph = Graph(vertices, edges)
    dist = floyd_warshall_apsp(graph)
    assert dist == expected_dist

@pytest.mark.parametrize("vertices, edges", [
    # Negative-weight cycle
    (['A', 'B', 'C'], [('A', 'B', -1), ('B', 'C', -2), ('C', 'A', -3)]),
    # Another negative-weight cycle
    (['A', 'B', 'C', 'D'], [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', -5), ('D', 'A', -4)]),
    # Add more cases with negative cycles
])
def test_floyd_warshall_negative_cycle(vertices, edges):
    graph = Graph(vertices, edges)
    with pytest.raises(ValueError, match='Graph contains a negative-weight cycle'):
        floyd_warshall_apsp(graph)
