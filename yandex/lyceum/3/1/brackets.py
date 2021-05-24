def bracket_check(s):
    def check():
        if len(s) % 2:
            return False
        _list = []
        for i in s:
            if i in "([{":
                _list.append(i)
            elif not _list or abs(ord(i) - ord(_list.pop())) > 2:
                return False
        return not _list

    if check():
        print("YES")
    else:
        print("NO")
