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

def get_strongly_connected_components(graph: Graph) -> List[List[str]]:
    """
    Finds strongly connected components in a directed graph using Kosaraju's algorithm.

    Parameters:
        graph (Graph): The graph to find SCCs in.

    Returns:
        List[List[str]]: A list of strongly connected components.

    Time complexity: O(V + E)
    """
    # First pass: Run DFS on the graph and store vertices by finish times
    _, _, finish_times, _ = dfs_helper(graph, None, None)
    vertices_by_finish_time = quick_sort(graph.vertices(), comparator=lambda v1, v2: finish_times[v1] > finish_times[v2])

    # Reverse the graph
    reversed_graph = graph.get_reversed()

    # Second pass: Run DFS on the reversed graph in order of decreasing finish times
    visited = {vertex: False for vertex in graph.vertices()}
    current_scc = []
    sccs = []

    def collect_scc(vertex: str, _: Optional[str]):
        nonlocal current_scc
        if visited[vertex]:
            return
        visited[vertex] = True
        current_scc.append(vertex)

    for vertex in vertices_by_finish_time:
        if not visited[vertex]:
            current_scc = []
            dfs_helper(reversed_graph, vertex, collect_scc)
            sccs.append(current_scc)

    return sccs