from collections import deque

n = int(input())
grid = []
coords = []

for i in range(n):
    coords.append(tuple(map(int, input().split())))

for i in range(n):
    temp = []
    for j in range(i):
        a = coords[i]
        b = coords[j]
        temp.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))
    grid.append(temp)

k = int(input())

for c in grid:
    for i in range(len(c)):
        c[i] = c[i] <= k

print(grid)
