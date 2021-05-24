import sys

for line in sys.stdin:
    print('= '.join(s for s in line.split() if not s.isalpha()))
