import sys
from collections import defaultdict

medicine = defaultdict(set)
for line in sys.stdin.readlines():
    v, k = line.rstrip().split(": ", 1)
    medicine[k].add(v)

for k, v in medicine.items():
    print(f"{k} - {' # '.join(v)}")
