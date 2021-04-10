def lengthOfLongestSubstring(s: str) -> int:
    ans, l, temp = 0, 0, 0
    d = dict()
    for r in range(len(s)):
        if s[r] in d:
            ans = max(ans, temp)
            n = d[s[r]] + 1
            for i in range(l, n):
                del d[s[i]]
                temp -= 1
            l = n
        d[s[r]] = r
        temp += 1
    ans = max(ans, temp)
    return len(s) if len(s) and not ans else ans

print(lengthOfLongestSubstring(input()))
