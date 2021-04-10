from itertools import combinations

def solution(n, m):
    keyrings = [[] for i in range(n)]
    for key, locations in enumerate(combinations(range(n), n - m + 1)):
        for location in locations:
            keyrings[location].append(key)
    return keyrings
