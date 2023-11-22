import pytest
from graph import Graph
from depth_first_search import get_strongly_connected_components

@pytest.mark.parametrize("vertices, edges, expected_sccs", [
    # Linear SCCs
    (['A', 'B', 'C'], [('A', 'B'), ('B', 'C')], [['A'], ['B'], ['C']]),

    # Two separate SCCs
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'A'), ('C', 'D'), ('D', 'C')], [['A', 'B'], ['C', 'D']]),

    # Complex SCCs
    (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
     [('A', 'B'), ('B', 'C'), ('C', 'A'), ('B', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'D'), ('G', 'F'), ('G', 'H'), ('H', 'G')],
     [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H']]),

    # No edges
    (['A', 'B', 'C'], [], [['A'], ['B'], ['C']])
])
def test_get_strongly_connected_components(vertices, edges, expected_sccs):
    graph = Graph(vertices, edges)

    sccs = get_strongly_connected_components(graph)

    # Sort the components and their contents for comparison
    sorted_sccs = sorted([sorted(scc) for scc in sccs])
    sorted_expected_sccs = sorted([sorted(scc) for scc in expected_sccs])

    assert sorted_sccs == sorted_expected_sccs
