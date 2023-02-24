#!/usr/bin/python3
"""_summary_"""


def pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
