from collections import Counter

x = input()
c = Counter(list(map(int, input().split())))
profit = 0

for i in range(int(input())):
    size, price = map(int, input().split())
    if(c[size] > 0):
        c[size] -= 1
        profit += price

print(profit)
