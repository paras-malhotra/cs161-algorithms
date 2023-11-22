from typing import Dict, Tuple
from priority_queue import PriorityQueue
from graph import Graph

def dijkstra_sssp(graph: Graph, source: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Dijkstra's algorithm for single-source shortest paths. This algorithm can only handle non-negative edge weights.

    Parameters:
        graph (Graph): The graph to traverse.
        source (str): The source vertex.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: The shortest distances to all vertices and their predecessors.

    Time complexity: O(V logV + E) where V is the number of vertices and E is the number of edges (if fibonacci heap is used).
    Space complexity: O(V) where V is the number of vertices.

    Note: This implementation uses a binary heap instead of a fibonacci heap, so the time complexity is O((V + E) logV).

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)])
    >>> dist, pred = dijkstra_sssp(graph, 'A')
    >>> dist['D']
    6
    >>> pred['D']
    'C'
    """
    # Initialize distance and predecessor dictionaries
    dist = {v: float('inf') for v in graph.vertices()}
    pred = {v: None for v in graph.vertices()}

    # Set the source distance to 0
    dist[source] = 0

    # Create a priority queue with the source vertex and its distance
    queue = PriorityQueue(lambda v1, v2: v1[1] < v2[1])
    queue.insert((source, 0))

    # Loop until the priority queue is empty
    while not queue.is_empty():
        # Get the current vertex and its distance
        current_vertex, current_dist = queue.extract_min()

        # Ignore the vertex if we have already found a shorter path since it was added to the priority queue
        if current_dist > dist[current_vertex]:
            continue

        # Loop through the neighbors of the current vertex
        for neighbor, weight in graph.neighbors(current_vertex):
            # Relax the distance to the neighbor
            new_dist = dist[current_vertex] + weight

            # Update the distance and predecessor if the new distance is less than the current distance
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                pred[neighbor] = current_vertex
                # We can afford to insert duplicates into the priority queue because we check if the distance is less than the current distance
                queue.insert((neighbor, dist[neighbor]))

    return dist, pred

def dijkstra_apsp(graph: Graph) -> Dict[str, Dict[str, float]]:
    """
    Dijkstra's algorithm for all-pairs shortest paths. This algorithm can only handle non-negative edge weights.

    Parameters:
        graph (Graph): The graph to traverse.

    Returns:
        Dict[str, Dict[str, float]]: The shortest distances between all pairs of vertices.

    Time complexity: O(V^2 logV + VE) where V is the number of vertices and E is the number of edges (if fibonacci heap is used).
    Space complexity: O(V^2) where V is the number of vertices.

    Note: This implementation uses a binary heap instead of a fibonacci heap, so the time complexity is O((V^2 + VE) logV).

    >>> graph = Graph(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)])
    >>> dist = djikstra_apsp(graph)
    >>> dist['A']['D']
    6
    """
    return {v: dijkstra_sssp(graph, v)[0] for v in graph.vertices()}