import pytest
from two_sat import two_sat

@pytest.mark.parametrize("variables,clauses,is_satisfiable", [
    (['x', 'y', 'z'], [('x', 'y'), ('y', 'z'), ('z', '~x')], True),
    (['x', 'y', 'z'], [('x', 'y'), ('y', 'z'), ('z', '~x'), ('~x', 'y'), ('y', 'x')], False),
    # Add more test cases here
])
def test_two_sat(variables, clauses, is_satisfiable):
    assert is_satisfiable == two_sat(variables, clauses)