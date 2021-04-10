def solution(n, l):
    cost = 0
    for i in range(n - 1):
        j = l.index(min(l[i:]))
        l[i:j+1] = reversed(l[i:j+1])
        cost += j - i + 1
    return cost

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        cost = solution(n, l)
        print("Case #{}: {}".format(t + 1, cost))
