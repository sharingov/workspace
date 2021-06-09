import sys

n = int(sys.stdin.readline().rstrip())
line1 = sys.stdin.readline().rstrip()
a, b = 0, 0
while line1 != "":
    line2 = sys.stdin.readline().rstrip()
    if len(set(line1) ^ set(line2)) > n:
        b += 1
    else:
        a += 1
    line1 = sys.stdin.readline().rstrip()

print(a, b, sep="\n")
