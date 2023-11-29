from graph import Graph
from strongly_connected_components import get_strongly_connected_components
from typing import List, Tuple, Dict

def two_sat(variables: List[str], clauses: List[Tuple[str, str]]) -> bool:
    """
    Identify whether a 2-SAT problem is satisfiable. The clauses must be in implicative normal form.

    Parameters:
        variables (List[str]): The variables of the 2-SAT problem.
        clauses (List[Tuple[str, str]]): The clauses of the 2-SAT problem. Each clause is a tuple of 2 variables where (x, y) means x => y (x implies y), i.e., clauses are in implicative normal form.

    Returns:
        bool: True if the 2-SAT problem is satisfiable, False otherwise.

    Time complexity: O(n + m) where n is the number of variables and m is the number of clauses.

    Examples:
        >>> two_sat(['x', 'y', 'z'], [('x', 'y'), ('y', 'z'), ('z', '~x')])
        True
        >>> two_sat(['x', 'y', 'z'], [('x', 'y'), ('y', 'z'), ('z', '~x'), ('~y', '~z')])
        True
        >>> two_sat(['x', 'y', 'z'], [('x', 'y'), ('y', 'z'), ('z', '~x'), ('~x', 'y'), ('y', 'x')])
        False
    """
    graph = Graph([])
    for variable in variables:
        graph.add_vertex(variable)
        graph.add_vertex(f'~{variable}')

    for clause in clauses:
        # Example: (x, y) means x => y
        graph.add_edge(clause[0], clause[1])

    strongly_connected_components = get_strongly_connected_components(graph)

    for component in strongly_connected_components:
        for vertex in component:
            # If a variable and its negation are in the same strongly connected component, the 2-SAT problem is unsatisfiable
            if vertex[0] == '~' and vertex[1:] in component:
                return False

    return True