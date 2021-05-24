n = int(input())
a = set()
for i in range(n):
    a.add(input())

m = int(input())
b = set()
for i in range(m):
    b.add(input())

for e in a ^ b:
    print(e)
