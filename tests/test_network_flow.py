import pytest
from network_flow import NetworkFlow, edmonds_karp

# Residual graph test data
residual_graph_test_data = [
    # Test case format: (vertices, capacities, array of flow tuples (v1, v2, flow), expected residual capacities after the flows are added)
    (
        ["A", "B", "C"],
        [("A", "B", 10), ("B", "C", 5)],
        [("A", "B", 3), ("B", "C", 3)],
        [("A", "B", 7), ("B", "A", 3), ("B", "C", 2), ("C", "B", 3)],
    ),
    (
        ["A", "B", "C", "D", "E"],
        [("A", "B", 5), ("B", "C", 15), ("B", "D", 5), ("C", "E", 10), ("D", "E", 10)],
        [("A", "B", 5), ("B", "C", 3), ("B", "D", 2), ("C", "E", 3), ("D", "E", 2)],
        [("B", "A", 5), ("B", "C", 12), ("C", "B", 3), ("B", "D", 3), ("D", "B", 2), ("C", "E", 7), ("E", "C", 3), ("D", "E", 8), ("E", "D", 2)],
    ),
    (
        ["A", "B", "C", "D", "E"],
        [("A", "B", 5), ("B", "A", 10), ("B", "C", 15), ("B", "D", 5), ("C", "E", 10), ("D", "E", 10)],
        [("A", "B", 5), ("B", "C", 3), ("B", "D", 2), ("C", "E", 3), ("D", "E", 2)],
        [("B", "A", 15), ("B", "C", 12), ("C", "B", 3), ("B", "D", 3), ("D", "B", 2), ("C", "E", 7), ("E", "C", 3), ("D", "E", 8), ("E", "D", 2)],
    ),
]

@pytest.mark.parametrize("vertices, capacities, flows, expected_residual_edges", residual_graph_test_data)
def test_residual_graph(vertices, capacities, flows, expected_residual_edges):
    # Create the network flow
    network = NetworkFlow(vertices, capacities)

    for (v1, v2, flow) in flows:
        # Add flow
        network.add_flow(v1, v2, flow)

    # Construct the residual graph
    residual_graph = network.get_residual_graph()

    # Extract edges from the residual graph
    residual_edges = residual_graph.edges()

    # Check if the residual graph's edges match the expected residual edges
    assert sorted(residual_edges) == sorted(expected_residual_edges)

# Max flow test data
max_flow_test_data = [
    # Test case format: (vertices, capacities, source, sink, expected max flow)
    (
        ["A", "B", "C"],
        [("A", "B", 10), ("B", "C", 5)],
        "A",
        "C",
        5,
    ),
    (
        ["A", "B", "C", "D", "E"],
        [("A", "B", 10), ("B", "C", 15), ("B", "D", 5), ("C", "E", 10), ("D", "E", 10)],
        "A",
        "E",
        10,
    ),
    (
        ["A", "B", "C", "D", "E"],
        [("A", "B", 5), ("B", "A", 10), ("B", "C", 15), ("B", "D", 5), ("C", "E", 10), ("D", "E", 10)],
        "A",
        "E",
        5,
    ),
]

@pytest.mark.parametrize("vertices, capacities, source, sink, expected_max_flow", max_flow_test_data)
def test_max_flow(vertices, capacities, source, sink, expected_max_flow):
    # Create the network flow
    network = NetworkFlow(vertices, capacities)

    # Compute the max flow
    max_flow = edmonds_karp(network, source, sink)

    # Check if the max flow matches the expected max flow
    assert max_flow == expected_max_flow