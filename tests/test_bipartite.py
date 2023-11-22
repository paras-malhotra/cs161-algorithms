import pytest
from graph import Graph
from breadth_first_search import check_bipartite

@pytest.mark.parametrize("vertices, edges, expected", [
    # Bipartite graphs
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D')], True),
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')], True),

    # Non-bipartite graphs
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D')], False),
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C')], False),

    # Disconnected graph with bipartite components
    (['A', 'B', 'C', 'D', 'E', 'F'], [('A', 'B'), ('C', 'D'), ('E', 'F')], True),

    # Disconnected graph with a non-bipartite component
    (['A', 'B', 'C', 'D', 'E', 'F'], [('A', 'B'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('E', 'C')], False),

    # Empty graph
    ([], [], True),

    # Single vertex graph
    (['A'], [], True),
])
def test_check_bipartite(vertices, edges, expected):
    graph = Graph(vertices, edges)
    assert check_bipartite(graph) == expected
