from collections import defaultdict

d = defaultdict(set)
for _ in range(int(input())):
    s = input().lower()
    d["".join(sorted(s))].add(s)

ans = []
for v in d.values():
    if len(v) > 1:
        ans.append(" ".join(sorted(v)))

ans.sort()
print(*ans, sep="\n")
