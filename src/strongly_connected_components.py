from typing import List, Optional
from graph import Graph
from depth_first_search import dfs_helper
from quick_sort import quick_sort

class SCCGraph(Graph):
    """
    A graph where each vertex represents a strongly connected component in the original graph.
    """
    def __init__(self, sccs: List[List[str]], original_graph: Graph):
        super().__init__(vertices=[str(i) for i in range(len(sccs))], undirected=False)
        self.sccs = sccs
        self.scc_mapping = {v: idx for idx, scc in enumerate(sccs) for v in scc}
        self.build_scc_graph(sccs, original_graph)

    """
    Build the SCC graph from the original graph and the list of SCCs.
    """
    def build_scc_graph(self, sccs: List[List[str]], original_graph: Graph):
        for scc_index, scc in enumerate(sccs):
            for vertex in scc:
                for neighbor, _ in original_graph.neighbors(vertex):
                    neighbor_scc_index = self.scc_mapping[neighbor]
                    if neighbor_scc_index != scc_index:
                        self.add_edge(str(scc_index), str(neighbor_scc_index))

    def get_scc_vertices(self, scc_index: int) -> List[str]:
        """
        Get the vertices in the original graph that form the SCC corresponding to the given SCC index in the SCC graph.

        Parameters:
            scc_index (int): The index of the SCC in the SCC graph.

        Returns:
            List[str]: A list of vertices in the original graph that form the specified SCC.
        """
        if scc_index < 0 or scc_index >= len(self.sccs):
            raise ValueError("Invalid SCC index")
        return self.sccs[scc_index]

    def get_scc_of_vertex(self, vertex: str) -> int:
        """
        Get the SCC index of a given vertex from the original graph.

        Parameters:
            vertex (str): The vertex in the original graph.

        Returns:
            int: The index of the SCC in the SCC graph that the vertex belongs to.
        """
        if vertex not in self.scc_mapping:
            raise ValueError("Vertex not found in the original graph")
        return self.scc_mapping[vertex]

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

def get_scc_graph(graph: Graph) -> SCCGraph:
    """
    Get the SCC graph of a given directed graph.

    Parameters:
        graph (Graph): The graph to find SCCs in.

    Returns:
        SCCGraph: The SCC graph of the given graph.
    """
    return SCCGraph(get_strongly_connected_components(graph), graph)