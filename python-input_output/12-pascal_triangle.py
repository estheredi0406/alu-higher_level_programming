#!/usr/bin/python3
"""defining function"""


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
