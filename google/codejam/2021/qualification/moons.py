import re

for t in range(int(input())):
    x, y, s = input().split()
    x, y = int(x), int(y)
    s = s.replace('?', '')
    pattern = 'J{2,}'
    s = re.sub(pattern, 'J', s)
    pattern = 'C{2,}'
    s = re.sub(pattern, 'C', s)
    if s and s[0] == 'J':
        x, y = y, x
    cost = len(s) // 2 * x + (abs(len(s) - 1)) // 2 * y
    print("Case #{}: {}".format(t + 1, cost))
