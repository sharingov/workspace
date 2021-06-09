def linear(some_list):
    temp = []
    if type(some_list) == list:
        for e in some_list:
            temp += linear(e)
    else:
        temp += [some_list]
    return temp
