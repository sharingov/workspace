for t in range(int(input())):
    n = int(input())
    grid, inverted = [], [[] for i in range(n)]
    k, r, c = 0, 0, 0
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(n):
            inverted[j].append(row[j])
        r += (len(row) > len(set(row)))
        k += row[i]
    for i in range(n):
        c += (len(inverted[i]) > len(set(inverted[i])))
    print("Case #{}:".format(t + 1), k, r, c)
