import pytest
from typing import List
from graph import Graph
from depth_first_search import depth_first_search, depth_first_search_entire_graph, topological_sort, get_bridge_edges

def test_depth_first_search():
    graph = Graph(['u', 'v', 'w', 'x', 'y', 'z'], [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'), ('w', 'z'), ('x', 'v'), ('y', 'x')])
    result = depth_first_search(graph, 'u')
    # Test that all reachable vertices have valid start and finish times
    assert all(result[vertex] for vertex in ['u', 'v', 'x', 'y'])
    # Test that unreachable vertices have None for start and finish times
    assert result['w'] == (None, None) and result['z'] == (None, None)

def test_depth_first_search_entire_graph():
    graph = Graph(['u', 'v', 'w', 'x', 'y', 'z'], [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'), ('w', 'z'), ('x', 'v'), ('y', 'x')])
    result = depth_first_search_entire_graph(graph)
    # Check that all vertices have valid times
    assert all(result[vertex][:2] for vertex in graph.vertices())
    # Check component numbers
    assert result['u'][2] == result['v'][2] == result['x'][2] == result['y'][2]
    assert result['w'][2] == result['z'][2]
    assert result['u'][2] != result['w'][2]

def is_valid_topological_order(graph: Graph, order: List[str]):
    position = {node: idx for idx, node in enumerate(order)}
    return all(position[u] < position[v] for u, v, _ in graph.edges())

@pytest.mark.parametrize("vertices, edges", [
    # Simple linear DAG
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D')]),
    # DAG with multiple paths
    (['A', 'B', 'C', 'D', 'E'], [('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]),
    # More complex DAG
    (['A', 'B', 'C', 'D', 'E', 'F'], [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')]),
    # Empty graph
    ([], []),
    # Single node graph
    (['A'], []),
])
def test_topological_sort(vertices, edges):
    graph = Graph(vertices, edges)
    order = topological_sort(graph)
    assert is_valid_topological_order(graph, order)

@pytest.mark.parametrize("vertices, edges, expected_bridges", [
    # Acyclic graph with two bridges
    (['A', 'B', 'C'], [('A', 'B'), ('B', 'C')], [('B', 'C'), ('A', 'B')]),

    # Case with no bridges
    (['A', 'B', 'C'], [('A', 'B'), ('B', 'C'), ('C', 'A')], []),

    # Cyclic graph with one bridges
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')], [('A', 'B')]),

    # Complex cyclic graph with one bridge
    (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('A', 'D'), ('B', 'C'), ('C', 'D'), ('D', 'E')], [('D', 'E')]),
])
def test_get_bridge_edges(vertices, edges, expected_bridges):
    graph = Graph(vertices, edges, undirected=True)
    bridges = get_bridge_edges(graph)

    # Sort bridges for comparison (since order doesn't matter in undirected graph)
    bridges_sorted = sorted(bridges, key=lambda x: (min(x), max(x)))
    expected_sorted = sorted(expected_bridges, key=lambda x: (min(x), max(x)))

    assert bridges_sorted == expected_sorted