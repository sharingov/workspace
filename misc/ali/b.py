vals = [int(input()) for _ in range(int(input()))]
x, y = map(int, input().split())
found = False
for i in vals:
    if i % x == 0 and i % y != 0:
        found = True
        print(i)
if not found:
    print(-1)
