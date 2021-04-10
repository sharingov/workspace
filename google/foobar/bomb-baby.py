def solution(x, y):
    x, y = [i for i in sorted((int(x), int(y)))]
    c = y//x - 1
    y = y%x + x
    while (x!=y):
        x, y = abs(x-y), min(x, y)
        c += 1
    return str(max(c, 0)) if x==1 else "impossible"

if __name__ == '__main__':
    print(solution(input(), input()))

