t = int(input())
for i in range(t):
    b = int(input().split()[1])
    c = 0
    for j in sorted(list(map(int, input().split()))):
        b -= j
        if b >= 0:
            c += 1
    print("Case #", i+1, ": ", c, sep="")
