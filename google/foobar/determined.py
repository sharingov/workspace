import random


def solution(l):
    l = [[i] for i in l]
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[j][0] % l[i][0] == 0:
                l[i].append(j)

    count = 0
    for i in l:
        for j in i[1:]:
            count += len(l[j])-1

    return count


if __name__ == '__main__':
    l = [random.randint(1, 99) for i in range(2000)]
    print(solution(l))
