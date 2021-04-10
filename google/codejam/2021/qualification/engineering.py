from itertools import permutations

def solution(n, l):
    cost = 0
    for i in range(n - 1):
        j = l.index(min(l[i:]))
        l[i:j+1] = reversed(l[i:j+1])
        cost += j - i + 1
    return cost

def func(n, c):
    if not (n - 1 <= c < 0.5 * (n ** 2) + 0.5 * n):
        return "IMPOSSIBLE"

    a = permutations(range(1, n + 1), n)
    for i in a:
        if solution(n, list(i)) == c:
            return ' '.join(map(str, i))


for t in range(int(input())):
    print("Case #{}: {}".format(t + 1, func(*map(int, input().split()))))
