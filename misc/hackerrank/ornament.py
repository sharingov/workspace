def print_rangoli(n):
    l = []
    for i in range(n*2-1):
        l.append([])
        for j in range(n*2-1):
            x = not ((i<n)^(j<n))
            val = abs(((n-1)*2)*x+(-1)**x*i-j)
            if val < n:
                l[i].append(chr(val+97))
    print(*('-'.join(i).center(4*n-3, '-') for i in l), sep = "\n")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
