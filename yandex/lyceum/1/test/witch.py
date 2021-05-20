a, b, c, d = input(), int(input()), int(input()), 3
if a == "ХОРОШЕЕ":
    d = 5
ans = []
for i in range(b, c + 1, d):
    ans.append(str(i))
print(' '.join(ans))
