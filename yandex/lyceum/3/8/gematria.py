import sys

print(
    *sorted(
        (line.rstrip() for line in sys.stdin.readlines()),
        key=lambda x: (sum(ord(r) - ord("A") + 1 for r in x.upper()), x),
    ),
    sep="\n"
)
