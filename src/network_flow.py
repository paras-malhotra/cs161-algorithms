from graph import Graph
from typing import Dict, List, Optional, Tuple, Callable
from breadth_first_search import breadth_first_search

class NetworkFlow(Graph):
    def __init__(self, vertices: List[str], edges: List[Tuple[str, str, Optional[float]]] = None):
        super().__init__(vertices, edges, undirected=False, default_weight=0)
        self.flow_network: Dict[str, Dict[str, float]] = {v: {u: 0 for u in vertices} for v in vertices}
        self.residual_graph: Graph = self.get_residual_graph()

    def add_flow(self, v1: str, v2: str, flow: float) -> None:
        """
        Add flow to an edge in the flow network. The flow is stored in flow_network[v1][v2] where v1 < v2.

        Parameters:
            v1 (str): The source vertex.
            v2 (str): The destination vertex.
            flow (float): The amount of flow to add.
        """
        current_flow = self.get_flow(v1, v2)

        if current_flow + flow < 0:
                return self.add_flow(v2, v1, -flow)

        if self.adj_matrix[v1][v2] != 0:
            if current_flow + flow <= self.adj_matrix[v1][v2]:
                if v1 < v2:
                    self.flow_network[v1][v2] += flow
                else:
                    self.flow_network[v2][v1] -= flow
                self.update_residual_graph(v1, v2)
            else:
                raise ValueError("Invalid flow addition: exceeds capacity.")
        else:
            raise ValueError("Invalid flow addition: nonexistent edge.")

    def add_flow_path(self, path: List[str], flow: float) -> None:
        """
        Add flow along a path in the flow network.

        Parameters:
            path (List[str]): The path (list of vertices) to add flow along.
            flow (float): The amount of flow to add.
        """
        for i in range(len(path) - 1):
            self.add_flow(path[i], path[i + 1], flow)

    def get_flow(self, v1: str, v2: str) -> float:
        """
        Get the flow from v1 to v2. The flow is returned as positive if it's from v1 to v2, and negative if from v2 to v1.

        Parameters:
            v1 (str): The source vertex.
            v2 (str): The destination vertex.

        Returns:
            float: The flow between v1 and v2.
        """
        if v1 > v2:
            # Return as negative if the flow is in the reverse direction
            return -self.flow_network[v2][v1]

        return self.flow_network[v1][v2]

    def get_residual_graph(self) -> Graph:
        """
        Create and return the residual graph based on current flows and capacities.

        Returns:
            Graph: The residual graph.
        """
        residual_edges = []
        for v1, v2, capacity in self.edges():
            flow = self.get_flow(v1, v2)
            residual_capacity = capacity - flow

            if flow < 0:
                # Skip edges with negative flow
                continue

            if flow > 0:
                # Add an edge in the reverse direction if there's flow
                residual_edges.append((v2, v1, flow + self.adj_matrix[v2][v1]))

            if residual_capacity > 0:
                # Add an edge in the forward direction if there's residual capacity
                residual_edges.append((v1, v2, residual_capacity))

        return Graph(self.vertices(), residual_edges)

    def update_residual_graph(self, v1: str, v2: str) -> None:
        """
        Dynamically update the residual graph after adding flow.

        Parameters:
            residual_graph (Graph): The residual graph to update.
            v1 (str): The source vertex.
            v2 (str): The destination vertex.
        """
        current_flow = self.get_flow(v1, v2)
        if current_flow < 0:
            return self.update_residual_graph(v2, v1)

        forward_capacity = self.adj_matrix[v1][v2] - current_flow
        backward_capacity = current_flow + self.adj_matrix[v2][v1]

        # Update forward edge, if any
        if forward_capacity > 0:
            self.residual_graph.add_edge(v1, v2, forward_capacity)
        else:
            self.residual_graph.remove_edge(v1, v2)

        # Update backward edge, if any
        if backward_capacity > 0:
            self.residual_graph.add_edge(v2, v1, backward_capacity)
        else:
            self.residual_graph.remove_edge(v2, v1)

def ford_fulkerson(network: NetworkFlow, source: str, sink: str, find_path: Callable[[Graph, str, str], Optional[List[str]]]) -> float:
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow from source to sink.

    Parameters:
        network (NetworkFlow): The flow network.
        source (str): The source vertex.
        sink (str): The sink vertex.
        find_path (Callable[[Graph, str, str], Optional[List[str]]]): The function to find an augmenting path in the residual graph. Takes the residual graph, source, and sink as parameters, and returns a list of vertices in the augmenting path.

    Returns:
        float: The maximum flow from source to sink.
    """
    # Initialize max flow to 0
    max_flow = 0

    # Find an augmenting path in the residual graph
    augmenting_path = find_path(network.get_residual_graph(), source, sink)

    # Iterate until no augmenting path can be found
    while augmenting_path is not None:
        # Find the maximum flow along the path based on the residual capacities
        min_flow_capacity = min([network.get_residual_graph().edge_weight(augmenting_path[i], augmenting_path[i + 1]) for i in range(len(augmenting_path) - 1)])

        # Add the maximum flow along the path to the network
        network.add_flow_path(augmenting_path, min_flow_capacity)

        # Add the maximum flow to the overall flow
        max_flow += min_flow_capacity

        # Find another augmenting path in the residual graph
        augmenting_path = find_path(network.get_residual_graph(), source, sink)

    # Return the maximum flow
    return max_flow

def find_path_bfs(residual_graph: Graph, source: str, sink: str) -> Optional[List[str]]:
    """
    Find an augmenting path in the residual graph using breadth-first search.

    Parameters:
        residual_graph (Graph): The residual graph.
        source (str): The source vertex.
        sink (str): The sink vertex.

    Returns:
        Optional[List[str]]: A list of vertices in the augmenting path, or None if no augmenting path exists.
    """
    # Find an augmenting path using breadth-first search
    pred = breadth_first_search(residual_graph, source)

    # If there's no path to the sink, return None
    if sink not in pred:
        return None

    # Otherwise, reconstruct the path from source to sink
    path = [sink]
    while path[-1] != source and path[-1] in pred:
        if pred[path[-1]] is None:
            return None
        path.append(pred[path[-1]])
    path.reverse()

    return path

def edmonds_karp(network: NetworkFlow, source: str, sink: str) -> float:
    """
    Implement the Edmonds-Karp algorithm to find the maximum flow from source to sink.

    Parameters:
        network (NetworkFlow): The flow network.
        source (str): The source vertex.
        sink (str): The sink vertex.

    Returns:
        float: The maximum flow from source to sink.

    Time complexity: O(V * E^2)
    Space complexity: O(V + E)

    Examples:
        >>> network = NetworkFlow(["A", "B", "C"], [("A", "B", 10), ("B", "C", 5)])
        >>> edmonds_karp(network, "A", "C")
        5
        >>> network = NetworkFlow(["A", "B", "C", "D", "E"], [("A", "B", 10), ("B", "C", 15), ("B", "D", 5), ("C", "E", 10), ("D", "E", 10)])
        >>> edmonds_karp(network, "A", "E")
        10
    """
    return ford_fulkerson(network, source, sink, find_path_bfs)