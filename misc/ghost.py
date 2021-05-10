def zeroes(_list):
    return sorted(_list, key=lambda x: x == 0)


def duplicate(_list):
    _set = set()
    for n in _list:
        if n not in _set:
            _set.add(n)
        else:
            return n


def trapezoid():
    try:
        a, b, h = map(int, input().split())
        if a <= 0 or b <= 0 or h <= 0:
            raise ValueError()
    except ValueError:
        print('Invalid input')
        return
    s = h*(a+b)
    if s % 2 == 0:
        print(s//2)
    else:
        print(s/2)


def robot(s):
    x, y = 0, 0
    for e in s:
        if e == 'U':
            y += 1
        elif e == 'D':
            y -= 1
        elif e == 'R':
            x += 1
        elif e == 'L':
            x -= 1
    return x == 0 and y == 0


def calc(s, n):
    exp = []
    ans = []
    for d in s:
        exp.append(d)
        exp.append('.')
    exp.pop()
    ops = ['', '+', '-', '*', '/']

    def solve():
        try:
            i = exp.index('.')
            for o in ops:
                exp[i] = o
                solve()
            exp[i] = '.'
        except ValueError:
            s = ''.join(exp)
            try:
                if eval(s) == n:
                    ans.append(s)
            except (ValueError, SyntaxError, ZeroDivisionError):
                pass
    solve()
    return ans
