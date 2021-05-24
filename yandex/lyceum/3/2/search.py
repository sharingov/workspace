def find_mountain(grid):
    x, y = 0, 0
    for i, line in enumerate(grid):
        for j, elem in enumerate(line):
            if elem > grid[x][y]:
                x, y = i, j
    return x, y
