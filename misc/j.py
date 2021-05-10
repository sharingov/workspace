a = input("Name of a tutor group: ")
b = int(input("Number of students: "))
c = int(input("Number of candidates: "))
candidates = {}
count = 0
winners = []

for i in range(c):
    candidates[input("Name of a candidate: ")] = 0

for i in range(b):
    name = input("Name of a candidate to vote for: ")
    if name in candidates:
        candidates[name] += 1
    else:
        count += 1

print("Group", a)
for i, j in candidates.items():
    if j == max(candidates.values()):
        winners.append(i)
    print(i, "got", j, "vote(s)")
print("Winner(s):", *winners, sep = '\n')
