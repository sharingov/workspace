def truth_hurts(tdlist, *args, **kwargs):
    temp = tdlist
    for arg in args:
        k = kwargs.get(arg[0])
        if k is not None:
            temp[arg[1]].sort(key=k)
    return temp
