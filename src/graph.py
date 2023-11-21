from typing import Dict, List, Tuple, Optional

class Graph:
    def __init__(self, vertices: List[str], edges: List[Tuple[str, str, Optional[float]]] = None, undirected: bool = False):
        """
        Initialize a graph with vertices and optional edges.

        Parameters:
            vertices (List[str]): List of vertex identifiers.
            edges (List[Tuple[str, str, float]]): Optional list of edges as tuples (v1, v2, weight).
            undirected (bool): Flag to indicate if the graph is undirected. Default is False (directed graph).
        """
        self.undirected = undirected
        self.adj_matrix: Dict[str, Dict[str, Optional[float]]] = {v: {u: float('inf') for u in vertices} for v in vertices}

        for v in vertices:
            self.adj_matrix[v][v] = 0

        if edges:
            for v1, v2, *weight in edges:
                self.add_edge(v1, v2, weight[0] if weight else None)

    def add_vertex(self, v: str) -> None:
        """
        Add a vertex to the graph.

        Parameters:
            v (str): Vertex identifier.
        """
        if v in self.adj_matrix:
            return  # Vertex already exists

        # Add the new vertex with infinite weights to others
        self.adj_matrix[v] = {u: float('inf') for u in self.adj_matrix}
        for u in self.adj_matrix:
            self.adj_matrix[u][v] = float('inf')
            self.adj_matrix[v][u] = float('inf')
        self.adj_matrix[v][v] = 0

    def remove_vertex(self, v: str) -> None:
        """
        Remove a vertex from the graph.

        Parameters:
            v (str): Vertex identifier.
        """
        del self.adj_matrix[v]
        for u in self.adj_matrix:
            del self.adj_matrix[u][v]

    def add_edge(self, v1: str, v2: str, weight: Optional[float] = None) -> None:
        """
        Add an edge to the graph.

        Parameters:
            v1 (str): The source vertex.
            v2 (str): The destination vertex.
            weight (float): Edge weight.
        """
        weight = weight if weight is not None else 1
        self.adj_matrix[v1][v2] = weight
        if self.undirected:
            self.adj_matrix[v2][v1] = weight

    def remove_edge(self, v1: str, v2: str) -> None:
        """
        Remove an edge from the graph.

        Parameters:
            v1 (str): The source vertex.
            v2 (str): The destination vertex.
        """
        self.adj_matrix[v1][v2] = float('inf')
        if self.undirected:
            self.adj_matrix[v2][v1] = float('inf')

    def edges(self) -> List[Tuple[str, str, float]]:
        """
        Get all edges in the graph.

        Returns:
            List[Tuple[str, str, float]]: A list of tuples, each containing a source vertex, a destination vertex, and the weight of the edge.
        """
        edge_list = []

        for v1 in self.vertices():
            for v2, weight in self.neighbors(v1):
                # For undirected graphs, consider each edge once
                if not self.undirected or v1 <= v2:
                    edge_list.append((v1, v2, weight))

        return edge_list

    def neighbors(self, vertex: str) -> List[Tuple[str, float]]:
        """
        Get all neighbors of a given vertex along with the weights of the connecting edges.

        Parameters:
            vertex (str): The vertex for which neighbors are required.

        Returns:
            List[Tuple[str, float]]: A list of tuples, each containing a neighbor vertex and the weight of the edge.
        """
        return [(v, weight) for v, weight in self.adj_matrix[vertex].items() if weight != float('inf') and v != vertex]

    def vertices(self) -> List[str]:
        """
        Get all vertices in the graph.

        Returns:
            List[str]: A list of vertices in the graph.
        """
        return list(self.adj_matrix.keys())

    def edge_weight(self, v1: str, v2: str) -> float:
        """
        Get the weight of an edge.

        Parameters:
            v1 (str): The source vertex.
            v2 (str): The destination vertex.

        Returns:
            float: The weight of the edge between v1 and v2.
        """
        return self.adj_matrix[v1][v2]

    def __str__(self) -> str:
        """
        String representation of the graph.

        Returns:
            str: A string representing the edges in the graph.
        """
        # Check if the graph is unweighted
        is_unweighted = all(weight in (1, float('inf')) for row in self.adj_matrix.values() for weight in row.values())

        edge_list = []

        for v1 in self.vertices():
            for v2, weight in self.neighbors(v1):
                # For undirected graphs, consider each edge once
                if not self.undirected or v1 <= v2:
                    edge = f"{v1}{v2}"
                    edge += f": {weight}" if not is_unweighted else ""
                    edge_list.append(edge)

        return ', '.join(edge_list)