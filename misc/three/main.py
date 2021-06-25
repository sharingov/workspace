import re

# print(sum(1 for c in input() if c.islower()))

s, sub = input(), input()
le = len(sub)
i = s.find(sub)
while i != -1:
    s = s[:i] + s[i + le :]
    i = s.find(sub)
print(s)


# print(sorted(re.findall(r"\w+", input()), key=len, reverse=True)[0])
