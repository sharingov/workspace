PI = 3.14159


def circle_length(r):
    return 2 * PI * r


def circle_area(r):
    return PI * r * r


def main():
    r = float(input())
    print(circle_length(r), circle_area(r))
