import sys

n = int(sys.stdin.readline())
se = set()
for _ in range(n):
    d = int(sys.stdin.readline())
    if d not in se:
        se.add(d)
        print(d)
