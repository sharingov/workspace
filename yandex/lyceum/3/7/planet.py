def find_farthest_orbit(list_of_orbits):
    ans = (0, 0)
    for a, b in list_of_orbits:
        if a != b and a * b > ans[0] * ans[1]:
            ans = (a, b)
    return ans
