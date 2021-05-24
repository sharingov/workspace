def golden_ratio(n):
    pre = 1
    last = 1
    for _ in range(1, n):
        pre, last = last, pre + last
    print(float(last / pre))
