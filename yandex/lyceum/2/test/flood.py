from collections import defaultdict

s = input()
ans = defaultdict(list)
while s:
    method, name = s.split(' - ')
    ans[name].append(method)
    s = input()

temp = sorted(ans.items())
for k, v in temp:
    print(k + ': ' + ', '.join(sorted(v, reverse=True)))
