from typing import List

def multiply_square_matrices(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiply two square matrices using the Strassen algorithm.

    Parameters:
        A (List[List[float]]): The first matrix.
        B (List[List[float]]): The second matrix.

    Returns:
        List[List[float]]: The product of A and B.

    Time complexity: O(n^2.81) where n is the number of rows/columns in the matrices.
    Space complexity: O(n) where n is the number of rows/columns in the matrices.

    Examples:
        >>> multiply_square_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
        >>> multiply_square_matrices([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
        [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]
    """
    n = len(A)

    # Raise an error if the matrices are not square or powers of 2
    if n != len(A[0]) or n != len(B) or n != len(B[0]) or n & (n - 1) != 0:
        raise ValueError("The matrices must be square and powers of 2")

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Split A into 4 submatrices
    A11 = [[A[i][j] for j in range(n // 2)] for i in range(n // 2)]
    A12 = [[A[i][j] for j in range(n // 2, n)] for i in range(n // 2)]
    A21 = [[A[i][j] for j in range(n // 2)] for i in range(n // 2, n)]
    A22 = [[A[i][j] for j in range(n // 2, n)] for i in range(n // 2, n)]

    # Split B into 4 submatrices
    B11 = [[B[i][j] for j in range(n // 2)] for i in range(n // 2)]
    B12 = [[B[i][j] for j in range(n // 2, n)] for i in range(n // 2)]
    B21 = [[B[i][j] for j in range(n // 2)] for i in range(n // 2, n)]
    B22 = [[B[i][j] for j in range(n // 2, n)] for i in range(n // 2, n)]

    # Calculate the 7 products of the 2x2 submatrices
    # P1 = A11 * (B12 - B22)
    P1 = multiply_square_matrices(A11, subtract_square_matrices(B12, B22))
    # P2 = (A11 + A12) * B22
    P2 = multiply_square_matrices(add_square_matrices(A11, A12), B22)
    # P3 = (A21 + A22) * B11
    P3 = multiply_square_matrices(add_square_matrices(A21, A22), B11)
    # P4 = A22 * (B21 - B11)
    P4 = multiply_square_matrices(A22, subtract_square_matrices(B21, B11))
    # P5 = (A11 + A22) * (B11 + B22)
    P5 = multiply_square_matrices(add_square_matrices(A11, A22), add_square_matrices(B11, B22))
    # P6 = (A12 - A22) * (B21 + B22)
    P6 = multiply_square_matrices(subtract_square_matrices(A12, A22), add_square_matrices(B21, B22))
    # P7 = (A11 - A21) * (B11 + B12)
    P7 = multiply_square_matrices(subtract_square_matrices(A11, A21), add_square_matrices(B11, B12))

    # Calculate the 4 quadrants of the solution matrix
    # C11 = P5 + P4 - P2 + P6
    C11 = add_square_matrices(subtract_square_matrices(add_square_matrices(P5, P4), P2), P6)
    # C12 = P1 + P2
    C12 = add_square_matrices(P1, P2)
    # C21 = P3 + P4
    C21 = add_square_matrices(P3, P4)
    # C22 = P5 + P1 - P3 - P7
    C22 = subtract_square_matrices(subtract_square_matrices(add_square_matrices(P5, P1), P3), P7)

    # Combine the 4 quadrants into the solution matrix
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n // 2):
        for j in range(n // 2):
            C[i][j] = C11[i][j]
            C[i][j + n // 2] = C12[i][j]
            C[i + n // 2][j] = C21[i][j]
            C[i + n // 2][j + n // 2] = C22[i][j]

    return C

def add_square_matrices(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Add two square matrices.

    Parameters:
        A (List[List[float]]): The first matrix.
        B (List[List[float]]): The second matrix.

    Returns:
        List[List[float]]: The sum of A and B.

    Time complexity: O(n^2) where n is the number of rows/columns in the matrices.
    Space complexity: O(n^2) where n is the number of rows/columns in the matrices.

    Examples:
        >>> add_square_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]
        >>> add_square_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    """
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def subtract_square_matrices(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Subtract two square matrices.

    Parameters:
        A (List[List[float]]): The first matrix.
        B (List[List[float]]): The second matrix.

    Returns:
        List[List[float]]: The difference of A and B.

    Time complexity: O(n^2) where n is the number of rows/columns in the matrices.
    Space complexity: O(n^2) where n is the number of rows/columns in the matrices.

    Examples:
        >>> subtract_square_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[-4, -4], [-4, -4]]
        >>> subtract_square_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]
    """
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]