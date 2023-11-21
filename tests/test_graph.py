import pytest
from graph import Graph

# Fixture for creating a basic graph
@pytest.fixture
def basic_graph():
    vertices = ['A', 'B', 'C', 'D']
    edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
    return Graph(vertices, edges)

# Test for adding a vertex
def test_add_vertex(basic_graph):
    basic_graph.add_vertex('E')
    assert 'E' in basic_graph.vertices()
    assert 'B' in basic_graph.vertices()

# Test for removing a vertex
def test_remove_vertex(basic_graph):
    basic_graph.remove_vertex('D')
    assert 'D' not in basic_graph.vertices()

# Test for adding an edge
def test_add_edge(basic_graph):
    basic_graph.add_edge('A', 'D', 4)
    assert ('D', 4) in basic_graph.neighbors('A')
    assert ('A', 4) not in basic_graph.neighbors('D')

# Test for removing an edge
def test_remove_edge(basic_graph):
    basic_graph.remove_edge('B', 'C')
    assert ('C', 2) not in basic_graph.neighbors('B')
    assert ('B', 2) not in basic_graph.neighbors('C')
    assert ('B', 1) in basic_graph.neighbors('A')

# Test for getting neighbors
def test_neighbors(basic_graph):
    neighbors = basic_graph.neighbors('B')
    assert len(neighbors) == 1
    assert ('C', 2) in neighbors

# Test for string representation of the graph
def test_str_representation(basic_graph):
    graph_str = str(basic_graph)
    assert 'AB: 1' in graph_str
    assert 'BC: 2' in graph_str
    assert 'CD: 3' in graph_str

# Test for undirected graph
def test_undirected_graph():
    vertices = ['A', 'B', 'C', 'D']
    edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
    undirected_graph = Graph(vertices, edges, undirected=True)
    undirected_graph.add_edge('C', 'A', 4)
    assert ('A', 4) in undirected_graph.neighbors('C')
    assert ('C', 4) in undirected_graph.neighbors('A')