from math import sqrt


def discriminant(a, b, c):
    return b * b - 4 * a * c


def larger_root(p, q):
    return (-p + sqrt(discriminant(1, p, q))) / 2


def smaller_root(p, q):
    return (-p - sqrt(discriminant(1, p, q))) / 2


def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
