#!/usr/bin/python3
""" returns perimeter of the island """


def island_perimeter(grid):
    """
    gives perimeter of island
    takes 1 args
    :grid -
    : 0 represents water
    : 1 represents land
    : each cell is square of side 1
    : cells are connected horizontally
    : grid is rectangularwith h & w < 100
    """

    perimeter = 0
    row = len(grid)
    column = len(grid[0])

    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
