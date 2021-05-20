s = input()
count = 0
while "дров" in s or "полен" in s:
    count += 1
    s = input()
print(count)
