import datetime as dt
import math


def convert(s):
    return dt.date(*map(int, reversed(s.split("."))))


def calculate(n, m):
    return round(math.sin((2 * math.pi * n.days) / m) * 100, 2)


interval = convert(input()) - convert(input())
print(
    calculate(-interval, 23),
    calculate(-interval, 28),
    calculate(-interval, 33),
    sep="\n",
)
