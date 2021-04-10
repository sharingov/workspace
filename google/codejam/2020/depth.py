for t in range(int(input())):
    s, result, n = input(), [], 0
    for digit in s:
        b = n - int(digit)
        n = int(digit)
        result.extend(")" * b + "(" * -b + digit)
    result.extend(")" * n)
    print("Case #", t + 1, ": ", "".join(result), sep="")
