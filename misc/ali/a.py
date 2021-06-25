n = 0
for i in range(1, int(input()) + 1):
    m = 0
    for c in str(i):
        m += int(c)
    if m % 4 == 0:
        n += 1

print(n)
