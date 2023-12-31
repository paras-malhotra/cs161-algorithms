from typing import Callable, Dict, Optional, Tuple, List
from graph import Graph
from quick_sort import quick_sort

def depth_first_search(graph: Graph, start: str, callback: Optional[Callable[[str, Optional[str]], None]] = None) -> Dict[str, Tuple[int, int]]:
    """
    Depth-first search (DFS) starting from a given vertex.

    Parameters:
        graph (Graph): The graph to search.
        start (str): The starting vertex.
        callback (Optional[Callable]): Optional callback function for each visited vertex.

    Returns:
        Dict[str, Tuple[int, int]]: Start and finish times for each vertex.

    Time complexity: O(V + E)

    >>> graph = Graph(['u', 'v', 'w', 'x', 'y', 'z'], [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'), ('w', 'z'), ('x', 'v'), ('y', 'x')])
    >>> depth_first_search(graph, 'u')
    {'u': (1, 8), 'v': (2, 7), 'x': (3, 6), 'y': (4, 5)}
    """
    visited, start_times, finish_times, _ = dfs_helper(graph, start, callback)
    return {vertex: (start_times[vertex], finish_times[vertex]) for vertex in visited}

def depth_first_search_entire_graph(graph: Graph, callback: Optional[Callable[[str, Optional[str]], None]] = None) -> Dict[str, Tuple[int, int, int]]:
    """
    Depth-first search (DFS) for the entire graph, including disconnected components.

    Parameters:
        graph (Graph): The graph to search.
        callback (Optional[Callable]): Optional callback function for each visited vertex.

    Returns:
        Dict[str, Tuple[int, int, int]]: Start and finish times, and component number for each vertex.

    Time complexity: O(V + E)

    >>> graph = Graph(['u', 'v', 'w', 'x', 'y', 'z'], [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'), ('w', 'z'), ('x', 'v'), ('y', 'x')])
    >>> depth_first_search_entire_graph(graph)
    {'u': (1, 8, 0), 'v': (2, 7, 0), 'w': (9, 12, 1), 'x': (3, 6, 0), 'y': (4, 5, 0), 'z': (10, 11, 1)}
    """
    visited, start_times, finish_times, component_numbers = dfs_helper(graph, None, callback)
    return {vertex: (start_times[vertex], finish_times[vertex], component_numbers[vertex]) for vertex in visited}

def dfs_helper(graph: Graph, start: Optional[str] = None, callback: Optional[Callable[[str, Optional[str]], None]] = None) -> Tuple[Dict[str, bool], Dict[str, int], Dict[str, int], Optional[Dict[str, int]]]:
    """
    Helper function for depth-first search.

    Parameters:
        graph (Graph): The graph to search.
        start (Optional[str]): The starting vertex, or None to search the entire graph.
        callback (Optional[Callable]): Optional callback function for each visited vertex.

    Returns:
        Tuple: Visited status, start times, finish times, and (optionally) component numbers.

    Time complexity: O(V + E)
    """
    visited, start_times, finish_times, component_numbers = {}, {}, {}, {}
    for vertex in graph.vertices():
        visited[vertex] = False
        start_times[vertex] = None
        finish_times[vertex] = None
        component_numbers[vertex] = None

    time, component_number = 0, 0

    def dfs_visit(vertex: str, parent: Optional[str]):
        nonlocal time, component_number
        time += 1
        start_times[vertex] = time
        visited[vertex] = True
        component_numbers[vertex] = component_number
        if callback:
            callback(vertex, parent)

        for neighbor, _ in graph.neighbors(vertex):
            if not visited[neighbor]:
                dfs_visit(neighbor, vertex)

        time += 1
        finish_times[vertex] = time

    if start is None:
        for vertex in graph.vertices():
            if not visited[vertex]:
                dfs_visit(vertex, None)
                component_number += 1
    else:
        dfs_visit(start, None)

    return visited, start_times, finish_times, component_numbers if start is None else None

def get_bridge_edges(graph: Graph) -> List[Tuple[str, str]]:
    """
    Find all bridge edges in an undirected graph using Tarjan's algorithm.

    Parameters:
        graph (Graph): The graph to search.

    Returns:
        List[Tuple[str, str]]: A list of bridge edges.

    Time complexity: O(V + E)
    """
    if not graph.undirected:
        raise ValueError('Graph must be undirected')

    # min_start_times[vertex] is the minimum start time of all vertices reachable from vertex except through vertex's parent
    start_times, min_start_times, visited, time = {}, {}, {vertex: False for vertex in graph.vertices()}, 0
    bridges = []

    def dfs_visit(vertex: str, parent: Optional[str]):
        nonlocal time
        time += 1
        start_times[vertex] = time
        min_start_times[vertex] = time
        visited[vertex] = True

        for neighbor, _ in graph.neighbors(vertex):
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                dfs_visit(neighbor, vertex)
                # Tree edge
                min_start_times[vertex] = min(min_start_times[vertex], min_start_times[neighbor])
                # If the child cannot reach any vertex with a lower start time than the current vertex, then the edge is a bridge
                if min_start_times[neighbor] > start_times[vertex]:
                    bridges.append((vertex, neighbor))
            else:
                # Back edge
                min_start_times[vertex] = min(min_start_times[vertex], start_times[neighbor])

    for vertex in graph.vertices():
        if not visited[vertex]:
            dfs_visit(vertex, None)

    return bridges

def topological_sort(graph: Graph) -> List[str]:
    """
    Topological sort of a directed acyclic graph (DAG).

    Parameters:
        graph (Graph): The graph to sort.

    Returns:
        List[str]: A topological ordering of the graph vertices.

    Time complexity: O(V log V + E)
    """
    _, _, finish_times, _ = dfs_helper(graph, None, None)
    return quick_sort(graph.vertices(), comparator=lambda v1, v2: finish_times[v1] > finish_times[v2])