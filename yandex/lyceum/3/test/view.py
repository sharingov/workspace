from statistics import mean

maps = [122, 13, 42, 1984, 66, 580]


def from_great_height():
    temp = sorted(maps, key=str)
    for i in range(len(temp)):
        t = []
        if i != 0:
            t.append(temp[i - 1])
        if i != len(temp) - 1:
            t.append(temp[i + 1])
        t.append(temp[i])
        maps[i] = round(mean(t))
