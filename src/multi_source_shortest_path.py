from graph import Graph
from typing import List, Optional, Tuple, Dict
from breadth_first_search import bfs_sssp
from dijkstra import dijkstra_sssp
from dag_shortest_path import dag_sssp
from bellman_ford import bellman_ford_sssp

def create_multi_source_node(graph: Graph, nodes: Optional[List[str]] = None, name: str = 'multi', weight: int = 0) -> str:
    """
    Create a new portal node in the graph that is connected to the specified nodes (or all nodes if None) with directed edges of the specified weight.

    Parameters:
        graph (Graph): The graph to modify.
        nodes (Optional[List[str]]): The nodes to connect to the new node. If None, connect to all nodes in the graph.
        name (str): The name of the new node.
        weight (int): The weight of the edges connecting the new node to the specified nodes.

    Returns:
        str: The name of the new node.
    """
    if nodes is None:
        nodes = graph.vertices()

    graph.add_vertex(name)
    for node in nodes:
        graph.add_edge(name, node, weight)

    return name

def bfs_mssp(graph: Graph, sources: List[str]) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Breadth-first search (BFS) algorithm for multi-source shortest paths.

    Parameters:
        graph (Graph): The graph to traverse.
        sources (List[str]): The source vertices.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(V * (V + E)) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'D')])
    >>> dist, pred = bfs_mssp(graph, ['A', 'B'])
    >>> dist['D']
    2
    >>> pred['D'], pred['C']
    'C', 'B'
    """
    create_multi_source_node(graph, sources, 'multi', 1)
    dist, pred = bfs_sssp(graph, 'multi')
    graph.remove_vertex('multi')

    # Subtract 1 from the distance to each destination to account for the extra edge weight added by the portal node.
    for destination in dist:
        dist[destination] -= 1

    for vertex in pred:
        if pred[vertex] == 'multi':
            pred[vertex] = None

    del dist['multi']
    del pred['multi']

    return dist, pred

def dijkstra_mssp(graph: Graph, sources: List[str]) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Dijkstra's algorithm for multi-source shortest paths.

    Parameters:
        graph (Graph): The graph to traverse.
        sources (List[str]): The source vertices.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(V * (V + E) * log(V)) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 3), ('C', 'D', 5)])
    >>> dist, pred = dijkstra_mssp(graph, ['A', 'B'])
    >>> dist['D']
    8
    >>> pred['D'], pred['C']
    'C', 'B'
    """
    create_multi_source_node(graph, sources, 'multi', 0)
    dist, pred = dijkstra_sssp(graph, 'multi')
    graph.remove_vertex('multi')

    for vertex in pred:
        if pred[vertex] == 'multi':
            pred[vertex] = None

    del dist['multi']
    del pred['multi']

    return dist, pred

def dag_mssp(graph: Graph, sources: List[str]) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    DAG shortest path algorithm for multi-source shortest paths.

    Parameters:
        graph (Graph): The graph to traverse.
        sources (List[str]): The source vertices.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(V * (V + E)) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 3), ('C', 'D', 5)])
    >>> dist, pred = dag_mssp(graph, ['A', 'B'])
    >>> dist['D']
    8
    >>> pred['D'], pred['C']
    'C', 'B'
    """
    create_multi_source_node(graph, sources, 'multi', 0)
    dist, pred = dag_sssp(graph, 'multi')
    graph.remove_vertex('multi')

    for vertex in pred:
        if pred[vertex] == 'multi':
            pred[vertex] = None

    del dist['multi']
    del pred['multi']

    return dist, pred

def bellman_ford_mssp(graph: Graph, sources: List[str]) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Bellman-Ford algorithm for multi-source shortest paths.

    Parameters:
        graph (Graph): The graph to traverse.
        sources (List[str]): The source vertices.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(V * (V + E)) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) where V is the number of vertices.

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 3), ('C', 'D', 5)])
    >>> dist, pred = bellman_ford_mssp(graph, ['A', 'B'])
    >>> dist['D']
    8
    >>> pred['D'], pred['C']
    'C', 'B'
    """
    create_multi_source_node(graph, sources, 'multi', 0)
    dist, pred = bellman_ford_sssp(graph, 'multi')
    graph.remove_vertex('multi')

    for vertex in pred:
        if pred[vertex] == 'multi':
            pred[vertex] = None

    del dist['multi']
    del pred['multi']

    return dist, pred