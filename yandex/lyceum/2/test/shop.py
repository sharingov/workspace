_set = set()

for s in input().split('; '):
    _set.update(s.split(': ')[1].split(', '))

_list = sorted(_set, reverse=True)
for i in range(len(_list)):
    if i % 2 == 1:
        _list[i] = _list[i].upper()

print(' - '.join(_list))
