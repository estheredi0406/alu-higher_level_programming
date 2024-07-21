#!/usr/bin/python3
"""defining function

"""
    Generates Pascal's Triangle up to the nth row.

    Parameters
    ----------
    n : int
        The number of rows to generate in Pascal's Triangle. Must be a positive integer.

    Returns
    -------
    list of list of int
        A list representing Pascal's Triangle, where each element is a list of integers representing a row.

    Raises
    ------
    ValueError
        If n is less than or equal to 0.

    Examples
    --------
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """"""


def pascal_function(n):
    """Represent Pascal's Triangle of size n.
    returns a list of lists of integers representing the triangle.
    """

    if n <= 0:
        return []
    
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles [-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + i])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
