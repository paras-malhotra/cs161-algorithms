import pytest
from kargers import kargers_min_cut_unweighted, Graph

# Test data for Karger's algorithm
kargers_test_data = [
    # Test case format: (vertices, edges, expected_min_cut)
    (
        ["A", "B", "C", "D"],
        [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C")],
        2,
    ),
    (
        ["A", "B", "C"],
        [("A", "B"), ("B", "C"), ("C", "A")],
        2,
    ),
    (
        ["A", "B", "C", "D"],
        [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C")],
        2,
    ),
    (
        ["A", "B", "C", "D", "E"],
        [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("B", "E"), ("C", "E")],
        2,
    ),
    (
        ["A", "B", "C", "D", "E", "F", "G", "H"],
        [("A", "B"), ("B", "F"), ("F", "E"), ("E", "A"), ("B", "C"), ("F", "G"), ("C", "D"), ("D", "H"), ("H", "G"), ("G", "C")],
        2,
    )
]

@pytest.mark.parametrize("vertices, edges, expected_min_cut", kargers_test_data)
def test_kargers_min_cut(vertices, edges, expected_min_cut):
    # Create the graph
    graph = Graph(vertices, edges, undirected=True)

    # Compute the min cut using Karger's algorithm
    min_cut = kargers_min_cut_unweighted(graph, None)

    # Check if the min cut matches the expected min cut
    assert min_cut == expected_min_cut
