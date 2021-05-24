def possible_turns(s: str):
    def convert(v):
        return (
            (ord(v[0]) - 64, int(v[1]))
            if type(v) == str
            else chr(v[0] + 64) + str(v[1])
        )

    x, y = convert(s)
    ans = []

    for i in range(1, 3):
        for j in range(-1, 2, 2):
            for k in range(-1, 2, 2):
                a = x + i * j
                b = y + k * (3 - abs(i))
                if 1 <= a <= 8 and 1 <= b <= 8:
                    ans.append(convert((a, b)))

    return sorted(ans)
