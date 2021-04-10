for i in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    m = 0
    for j in range(n // 2):
        if s[j] != s[n - j - 1]:
            m += 1
    print("Case #{}: {}".format(i + 1, abs(k - m)))
