def late(now, classes, bus):
    def convert(s):
        return int(s[:-3]) * 60 + int(s[3:])

    diff = convert(classes) - convert(now)
    for n in bus[::-1]:
        if n < 5:
            break
        if n + 15 <= diff:
            n -= 5
            return f"Выйти через {n} минут"
    return "Опоздание"
