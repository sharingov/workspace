import textwrap

def merge_the_tools(string, k):
    l = []
    t = textwrap.wrap(string, k)
    for i in range(len(string)//k):
        l.append([])
        l[i].extend(j for j in t[i] if j not in l[i])
    print(*(''.join(i) for i in l), sep = '\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
