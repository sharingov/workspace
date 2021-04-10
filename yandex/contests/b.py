import sys

n = int(sys.stdin.readline())
val = ans = 0
for _ in range(n):
    d = int(sys.stdin.readline())
    if d:
        val += 1
        ans = max(ans, val)
    else:
        val = 0

print(ans)
