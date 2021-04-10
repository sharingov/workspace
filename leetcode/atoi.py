import re

def myAtoi(s: str) -> int:
    match = re.search('^[+|-]?\d+', s.lstrip())
    return (match or 0) and max(-2147483648, min(2147483647, int(match.group())))
