#!/usr/bin/python3
""" pascal trianle"""
def pascal_triangle(n):
    """ functuion to return pascals triangle """
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        row = [1]

        if i > 0:
            for j in range(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            row.append(1)
        pascal.append(row)
    return pascal
