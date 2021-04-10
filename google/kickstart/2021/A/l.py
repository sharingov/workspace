for t in range(int(input())):
    r, c = list(map(int, input().split()))
    grid = []
    total = 0
    for i in range(r):
        grid.append(list(map(int, input().split())))
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                for xdir in range(-1, 2, 2):
                    xlen = 1
                    for x in range(j + xdir, -1 if (xdir - 1) else c, xdir):
                        if grid[i][x]:
                            xlen += 1
                            for ydir in range(-1, 2, 2):
                                ylen = 1
                                for y in range(i + ydir, -1 if (ydir - 1) else r, ydir):
                                    if grid[y][x]:
                                        ylen += 1
                                    else:
                                        break
                                    if xlen / ylen == 2:
                                        total += 1
                                    if ylen / xlen == 2:
                                        total += 1
                                        break
                        else:
                            break
    print("Case #{}: {}".format(t + 1, total))
