import statistics
import sys

heights = [int(line) for line in sys.stdin.readlines()]
print(statistics.mean(heights) if heights else -1)
