import pytest
from graph import Graph
from strongly_connected_components import get_strongly_connected_components, get_scc_graph

@pytest.mark.parametrize("vertices, edges, expected_sccs, expected_scc_edges", [
    # Linear SCCs
    (['A', 'B', 'C'], [('A', 'B'), ('B', 'C')], [['A'], ['B'], ['C']], [(0, 1), (1, 2)]),

    # Two separate SCCs
    (['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'A'), ('C', 'D'), ('D', 'C')], [['A', 'B'], ['C', 'D']], []),

    # Complex SCCs
    (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
     [('A', 'B'), ('B', 'C'), ('C', 'A'), ('B', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'D'), ('G', 'F'), ('G', 'H'), ('H', 'G')],
     [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H']], [(0, 1), (2, 1)]),

    # No edges
    (['A', 'B', 'C'], [], [['A'], ['B'], ['C']], []),
])
def test_get_strongly_connected_components(vertices, edges, expected_sccs, expected_scc_edges):
    graph = Graph(vertices, edges)

    sccs = get_strongly_connected_components(graph)
    scc_graph = get_scc_graph(graph)

    # Sort the components and their contents for comparison
    sorted_sccs = sorted([sorted(scc) for scc in sccs])
    sorted_expected_sccs = sorted([sorted(scc) for scc in expected_sccs])

    assert sorted_sccs == sorted_expected_sccs

    # Check the edges in the SCC graph
    actual_scc_edges = set()
    for u in scc_graph.vertices():
        for v, _ in scc_graph.neighbors(u):
            actual_scc_edges.add((tuple(sorted(scc_graph.get_scc_vertices(int(u)))), tuple(sorted(scc_graph.get_scc_vertices(int(v))))))

    expected_scc_edgeset = set()
    for u, v in expected_scc_edges:
        expected_scc_edgeset.add((tuple(sorted(expected_sccs[u])), tuple(sorted(expected_sccs[v]))))

    assert actual_scc_edges == expected_scc_edgeset
