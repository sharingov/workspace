import sys

print(
    *(
        f"Line {i+1}: {line.strip()[1:].lstrip()}"
        for i, line in enumerate(sys.stdin.readlines())
        if line.lstrip()[0] == "#"
    ),
    sep="\n",
)
