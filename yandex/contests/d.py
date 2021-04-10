import sys

def sol(debt, space):
    if debt == space:
        return [')' * space]
    a = list(map(lambda x: '(' + x, sol(debt + 1, space - 1)))
    if debt:
        b = list(map(lambda x: ')' + x, sol(debt - 1, space - 1)))
        return a + b
    return a

n = int(sys.stdin.readline())
ans = sol(0, n * 2)
for e in ans:
    print(e)
